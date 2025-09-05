#!/usr/bin/env python3
"""
Основной скрипт для перевода документации.
Обрабатывает .md файлы и .png изображения.
"""

import os
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Опциональные импорты для функций AI
try:
    import torch
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False
    logger.warning("Transformers не установлен. AI перевод недоступен.")

# Опциональные импорты для OCR
try:
    import cv2
    import numpy as np
    from PIL import Image
    import pytesseract
    HAS_OCR = True
except ImportError:
    HAS_OCR = False
    logger.warning("OCR библиотеки не установлены. Обработка изображений ограничена.")

from shutil import copyfile


def load_glossary(glossary_path: Optional[str]) -> Dict[str, str]:
    """Загрузка глоссария для специальных терминов"""
    if not glossary_path or not os.path.exists(glossary_path):
        return {}
    
    try:
        with open(glossary_path, 'r', encoding='utf-8') as f:
            glossary = json.load(f)
            logger.info(f"Загружен глоссарий с {len(glossary)} терминами")
            return glossary
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Ошибка загрузки глоссария: {e}")
        return {}


def apply_glossary(text: str, glossary: Dict[str, str]) -> str:
    """Применение глоссария к тексту"""
    if not glossary:
        return text
    
    for term, translation in glossary.items():
        # Используем word boundaries для точного совпадения
        pattern = r'\b' + re.escape(term) + r'\b'
        text = re.sub(pattern, translation, text, flags=re.IGNORECASE)
    
    return text


def preserve_markdown_elements(text: str) -> Tuple[str, Dict[str, str]]:
    """Сохранение элементов разметки от перевода"""
    placeholders = {}
    counter = 0
    
    patterns = [
        (r'```[\s\S]*?```', 'CODE_BLOCK'),          # Блоки кода
        (r'`[^`\n]+`', 'INLINE_CODE'),              # Встроенный код
        (r'\[([^\]]*)\]\(([^)]*)\)', 'LINK'),       # Ссылки
        (r'<!--[\s\S]*?-->', 'COMMENT'),            # HTML комментарии
        (r'<[^>]+>', 'HTML_TAG'),                   # HTML теги
        (r'\!\[([^\]]*)\]\(([^)]*)\)', 'IMAGE'),    # Изображения
        (r'\{%[\s\S]*?%\}', 'TEMPLATE'),            # Шаблонные конструкции
        (r'\$\$[\s\S]*?\$\$', 'MATH_BLOCK'),        # LaTeX блоки
        (r'\$[^$\n]+\$', 'MATH_INLINE'),            # Inline LaTeX
    ]
    
    for pattern, element_type in patterns:
        def replace_func(match):
            nonlocal counter
            placeholder = f'__PLACEHOLDER_{element_type}_{counter}__'
            placeholders[placeholder] = match.group(0)
            counter += 1
            return placeholder
        
        text = re.sub(pattern, replace_func, text)
    
    return text, placeholders


def restore_preserved_elements(text: str, placeholders: Dict[str, str]) -> str:
    """Восстановление сохраненных элементов"""
    for placeholder, original in placeholders.items():
        text = text.replace(placeholder, original)
    return text


def translate_text_simple(text: str, glossary: Optional[Dict[str, str]] = None) -> str:
    """Простой перевод без AI модели (заглушка)"""
    if not text.strip():
        return text
    
    # Применяем глоссарий
    if glossary:
        text = apply_glossary(text, glossary)
    
    # Для демонстрации - здесь может быть API вызов к внешнему сервису
    # Или другая логика перевода
    logger.info("Используется простой режим перевода (заглушка)")
    return text  # Возвращаем оригинальный текст


def translate_text_ai(text: str, model, tokenizer, glossary: Optional[Dict[str, str]] = None, max_length: int = 512) -> str:
    """Перевод текста с использованием AI модели"""
    if not text.strip():
        return text
    
    # Применяем глоссарий
    if glossary:
        text = apply_glossary(text, glossary)
    
    # Сохраняем элементы разметки
    text_to_translate, placeholders = preserve_markdown_elements(text)
    
    # Пропускаем перевод, если нечего переводить
    if not text_to_translate.strip():
        return text
    
    try:
        # Разбиваем длинный текст на части
        chunks = []
        sentences = re.split(r'(?<=[.!?])\s+', text_to_translate)
        
        current_chunk = ""
        for sentence in sentences:
            if len(current_chunk + sentence) > max_length:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = sentence
                else:
                    # Если одно предложение слишком длинное
                    chunks.append(sentence[:max_length])
            else:
                current_chunk += " " + sentence if current_chunk else sentence
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        translated_chunks = []
        for chunk in chunks:
            if not chunk.strip():
                translated_chunks.append(chunk)
                continue
                
            # Перевод с русского на английский
            inputs = tokenizer(
                chunk, 
                return_tensors="pt", 
                padding=True, 
                truncation=True,
                max_length=max_length
            ).to(model.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_length,
                    num_beams=4,
                    early_stopping=True,
                    temperature=0.7
                )
            
            translated_chunk = tokenizer.decode(outputs[0], skip_special_tokens=True)
            translated_chunks.append(translated_chunk)
        
        translated_text = " ".join(translated_chunks)
        
        # Восстанавливаем сохраненные элементы
        translated_text = restore_preserved_elements(translated_text, placeholders)
        
        return translated_text
    
    except Exception as e:
        logger.error(f"Ошибка AI перевода: {e}")
        return text  # Возвращаем оригинальный текст в случае ошибки


def process_markdown_file(src_path: str, dest_path: str, model, tokenizer, glossary: Dict[str, str]) -> bool:
    """Обработка Markdown файла"""
    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Создаем директорию если не существует
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        if model and tokenizer:
            translated_content = translate_text_ai(content, model, tokenizer, glossary)
        else:
            translated_content = translate_text_simple(content, glossary)
        
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        logger.info(f"✓ Переведен: {src_path} -> {dest_path}")
        return True
        
    except Exception as e:
        logger.error(f"✗ Ошибка обработки файла {src_path}: {e}")
        return False


def extract_text_from_image(image_path: str, lang: str = 'rus') -> Tuple[str, Optional[Image.Image]]:
    """Извлечение текста с изображения с помощью Tesseract OCR"""
    if not HAS_OCR:
        logger.warning("OCR недоступен - возвращаем пустой текст")
        return "", None
        
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang=lang)
        return text.strip(), image
    except Exception as e:
        logger.error(f"Ошибка извлечения текста из {image_path}: {e}")
        return "", None


def overlay_text_on_image(image: Image.Image, translated_text: str) -> Optional[Image.Image]:
    """Наложение переведенного текста на изображение"""
    if not HAS_OCR:
        return image
        
    try:
        # Конвертируем PIL Image в OpenCV format
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Добавляем белую полосу снизу для перевода
        height, width = image_cv.shape[:2]
        text_height = 100
        new_height = height + text_height
        new_image = np.ones((new_height, width, 3), dtype=np.uint8) * 255
        new_image[:height, :] = image_cv
        
        # Разбиваем текст на строки для корректного отображения
        words = translated_text.split()
        lines = []
        current_line = ""
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        thickness = 1
        
        max_width = width - 20  # Отступы по бокам
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            text_size = cv2.getTextSize(test_line, font, font_scale, thickness)[0]
            
            if text_size[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                    current_line = word
                else:
                    lines.append(word)  # Слово слишком длинное, но добавляем
        
        if current_line:
            lines.append(current_line)
        
        # Отображаем строки
        line_height = 20
        start_y = height + 25
        
        for i, line in enumerate(lines[:3]):  # Максимум 3 строки
            y = start_y + i * line_height
            cv2.putText(
                new_image,
                line,
                (10, y),
                font,
                font_scale,
                (0, 0, 0),
                thickness,
                cv2.LINE_AA
            )
        
        return Image.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
        
    except Exception as e:
        logger.error(f"Ошибка наложения текста: {e}")
        return image


def process_image_file(src_path: str, dest_path: str, model=None, tokenizer=None, glossary: Optional[Dict[str, str]] = None) -> bool:
    """Обработка изображения"""
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Если OCR недоступен, просто копируем файл
        if not HAS_OCR:
            copyfile(src_path, dest_path)
            logger.info(f"✓ Скопировано изображение: {src_path} -> {dest_path}")
            return True
        
        # Извлекаем текст с изображения
        original_text, image = extract_text_from_image(src_path)
        
        if not original_text or not image:
            # Если текст не найден, просто копируем изображение
            copyfile(src_path, dest_path)
            logger.info(f"✓ Скопировано изображение (текст не найден): {src_path} -> {dest_path}")
            return True
        
        # Переводим извлеченный текст
        if model and tokenizer:
            translated_text = translate_text_ai(original_text, model, tokenizer, glossary)
        else:
            translated_text = translate_text_simple(original_text, glossary)
        
        # Создаем новое изображение с переведенным текстом
        new_image = overlay_text_on_image(image, translated_text)
        
        if new_image:
            new_image.save(dest_path)
            logger.info(f"✓ Обработано изображение с текстом: {src_path} -> {dest_path}")
        else:
            copyfile(src_path, dest_path)
            logger.info(f"✓ Скопировано изображение: {src_path} -> {dest_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Ошибка обработки изображения {src_path}: {e}")
        return False


def should_process_file(src_path: str, dest_path: str, force: bool = False) -> bool:
    """Проверка, нужно ли обрабатывать файл"""
    if force:
        return True
        
    if not os.path.exists(dest_path):
        return True
    
    # Обрабатываем, если исходный файл новее целевого
    return os.path.getmtime(src_path) > os.path.getmtime(dest_path)


def load_translation_model():
    """Загрузка модели перевода"""
    if not HAS_TRANSFORMERS:
        logger.warning("Transformers не установлен, AI перевод недоступен")
        return None, None
    
    model_name = "Helsinki-NLP/opus-mt-ru-en"
    logger.info(f"Загрузка модели {model_name}...")
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Проверяем доступность GPU
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = model.to(device)
        logger.info(f"Модель загружена на {device.upper()}")
        
        return model, tokenizer
        
    except Exception as e:
        logger.error(f"Ошибка загрузки модели: {e}")
        return None, None


def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(description='Translate documentation from Russian to English')
    parser.add_argument('--source_dir', default='./ru', help='Source directory with Russian content')
    parser.add_argument('--target_dir', default='./en', help='Target directory for English content')
    parser.add_argument('--glossary', help='Path to glossary JSON file')
    parser.add_argument('--force', action='store_true', help='Force reprocessing of all files')
    parser.add_argument('--no-ai', action='store_true', help='Disable AI translation')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Проверяем существование исходной директории
    if not os.path.exists(args.source_dir):
        logger.error(f"Исходная директория не существует: {args.source_dir}")
        return False
    
    # Загружаем глоссарий
    glossary = load_glossary(args.glossary)
    
    # Инициализация модели перевода
    model, tokenizer = None, None
    if not args.no_ai:
        model, tokenizer = load_translation_model()
    
    processed_count = 0
    error_count = 0
    skipped_count = 0
    
    # Рекурсивный обход исходной директории
    for root, dirs, files in os.walk(args.source_dir):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, args.source_dir)
            dest_path = os.path.join(args.target_dir, rel_path)
            
            # Пропускаем скрытые файлы и системные файлы
            if file.startswith('.') or file in ['Thumbs.db', '.DS_Store']:
                continue
            
            # Проверяем, нужно ли обрабатывать файл
            if not should_process_file(src_path, dest_path, args.force):
                skipped_count += 1
                continue
            
            # Обрабатываем файлы
            success = False
            if file.endswith('.md'):
                success = process_markdown_file(src_path, dest_path, model, tokenizer, glossary)
            elif file.endswith(('.png', '.jpg', '.jpeg')):
                success = process_image_file(src_path, dest_path, model, tokenizer, glossary)
            else:
                # Копируем другие файлы как есть
                try:
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    copyfile(src_path, dest_path)
                    logger.info(f"✓ Скопирован: {src_path} -> {dest_path}")
                    success = True
                except Exception as e:
                    logger.error(f"✗ Ошибка копирования {src_path}: {e}")
                    success = False
            
            if success:
                processed_count += 1
            else:
                error_count += 1
    
    logger.info(f"Обработка завершена. Успешно: {processed_count}, Ошибок: {error_count}, Пропущено: {skipped_count}")
    return error_count == 0


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.info("Прервано пользователем")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        sys.exit(1)
