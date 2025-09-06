#!/usr/bin/env python3

"""
Основной скрипт для перевода документации.
Обрабатывает .md файлы и .png изображения с ограничением количества файлов.
"""

import os
import argparse
import json
import re
import sys
import time
import gc
from pathlib import Path
from typing import Dict, Optional, Tuple, List
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Опциональные импорты для мониторинга ресурсов
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False
    logger.warning("psutil не установлен. Мониторинг ресурсов недоступен.")

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

class TranslationConfig:
    """Класс для управления конфигурацией перевода"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_default_config()
        if config_path and os.path.exists(config_path):
            self._load_config(config_path)
    
    def _load_default_config(self) -> Dict:
        """Загрузка конфигурации по умолчанию"""
        return {
            "limits": {
                "max_files_per_run": 20,
                "max_chars_per_chunk": 10000,
                "max_tokens_per_input": 512,
                "max_file_size_bytes": 1048576,
                "timeout_per_file_seconds": 300
            }
        }
    
    def _load_config(self, config_path: str):
        """Загрузка конфигурации из файла"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                file_config = json.load(f)
                # Обновляем только существующие ключи
                for key, value in file_config.items():
                    if key in self.config:
                        if isinstance(value, dict) and isinstance(self.config[key], dict):
                            self.config[key].update(value)
                        else:
                            self.config[key] = value
            logger.info(f"Конфигурация загружена из {config_path}")
        except Exception as e:
            logger.warning(f"Ошибка загрузки конфигурации: {e}. Используется конфигурация по умолчанию.")
    
    def get(self, *keys):
        """Получение значения из конфигурации по ключам"""
        value = self.config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        return value

class ResourceMonitor:
    """Класс для мониторинга системных ресурсов"""
    
    def __init__(self, memory_limit_mb: int = 2048):
        self.memory_limit_mb = memory_limit_mb
        self.start_time = time.time()
    
    def check_memory_usage(self) -> bool:
        """Проверка использования памяти"""
        if not HAS_PSUTIL:
            return True
        
        try:
            process = psutil.Process()
            memory_mb = process.memory_info().rss / 1024 / 1024
            
            if memory_mb > self.memory_limit_mb:
                logger.warning(f"Превышен лимит памяти: {memory_mb:.1f}MB > {self.memory_limit_mb}MB")
                return False
            
            return True
        except Exception as e:
            logger.warning(f"Ошибка мониторинга памяти: {e}")
            return True
    
    def get_elapsed_time(self) -> float:
        """Получение времени выполнения"""
        return time.time() - self.start_time
    
    def cleanup(self):
        """Очистка памяти"""
        gc.collect()
        if HAS_TRANSFORMERS and torch.cuda.is_available():
            torch.cuda.empty_cache()

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
        # Используем более точное сопоставление
        pattern = r'\b' + re.escape(term) + r'\b'
        text = re.sub(pattern, translation, text, flags=re.IGNORECASE)
    
    return text

def preserve_markdown_elements(text: str) -> Tuple[str, Dict[str, str]]:
    """Сохранение элементов разметки от перевода"""
    placeholders = {}
    counter = 0
    
    # Исправленные паттерны для элементов Markdown
    patterns = [
        (r'```[\s\S]*?```', 'CODE_BLOCK'),  # Исправлено: блоки кода
        (r'`[^`\n]+`', 'INLINE_CODE'),
        (r'\[([^\]]*)\]\(([^)]*)\)', 'LINK'),
        (r'<!--[\s\S]*?-->', 'COMMENT'),
        (r'<[^>]+>', 'HTML_TAG'),
        (r'!\[([^\]]*)\]\(([^)]*)\)', 'IMAGE'),  # Исправлено: изображения
        (r'\{%[\s\S]*?%\}', 'TEMPLATE'),
        (r'\$\$[\s\S]*?\$\$', 'MATH_BLOCK'),
        (r'\$[^$\n]+\$', 'MATH_INLINE'),
        (r'#+\s+[^\n]+', 'HEADER'),  # Заголовки
        (r'\|[^\n]+\|', 'TABLE_ROW'),  # Строки таблиц
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
    """Восстановление сохранённых элементов"""
    for placeholder, original in placeholders.items():
        text = text.replace(placeholder, original)
    return text

def translate_text_simple(text: str, glossary: Optional[Dict[str, str]] = None) -> str:
    """Простой перевод без AI модели (заглушка)"""
    if not text.strip():
        return text
    
    if glossary:
        text = apply_glossary(text, glossary)
    
    logger.debug("Используется простой режим перевода (заглушка)")
    return text

def translate_text_ai(text: str, model, tokenizer, glossary: Optional[Dict[str, str]] = None, 
                     max_length: int = 512, timeout: int = 300) -> str:
    """Перевод текста с использованием AI модели с таймаутом"""
    if not text.strip():
        return text
    
    start_time = time.time()
    
    try:
        # Применяем глоссарий до сохранения элементов разметки
        if glossary:
            text = apply_glossary(text, glossary)
        
        # Сохраняем элементы разметки
        text_to_translate, placeholders = preserve_markdown_elements(text)
        
        if not text_to_translate.strip():
            return text
        
        # Разбиваем текст на части
        chunks = []
        sentences = re.split(r'(?<=[.!?])\s+', text_to_translate)
        current_chunk = ""
        
        for sentence in sentences:
            # Проверка таймаута
            if time.time() - start_time > timeout:
                logger.warning("Превышен таймаут перевода")
                break
            
            if len(current_chunk + sentence) > max_length:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = sentence
                else:
                    # Разбиваем слишком длинное предложение
                    chunks.append(sentence[:max_length])
            else:
                current_chunk += " " + sentence if current_chunk else sentence
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        # Ограничиваем количество частей
        if len(chunks) > 50:  # Максимум 50 частей
            logger.warning(f"Текст разбит на {len(chunks)} частей, ограничиваем до 50")
            chunks = chunks[:50]
        
        translated_chunks = []
        
        for i, chunk in enumerate(chunks):
            # Проверка таймаута для каждой части
            if time.time() - start_time > timeout:
                logger.warning("Превышен таймаут перевода")
                break
            
            if not chunk.strip():
                translated_chunks.append(chunk)
                continue
            
            try:
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
                        num_beams=3,  # Уменьшено для производительности
                        early_stopping=True,
                        temperature=0.7,
                        do_sample=False
                    )
                
                translated_chunk = tokenizer.decode(outputs[0], skip_special_tokens=True)
                translated_chunks.append(translated_chunk)
                
                # Логируем прогресс каждые 10 частей
                if (i + 1) % 10 == 0:
                    logger.debug(f"Переведено {i + 1}/{len(chunks)} частей")
                
            except Exception as e:
                logger.warning(f"Ошибка перевода части {i + 1}: {e}")
                translated_chunks.append(chunk)  # Возвращаем оригинал при ошибке
        
        # Объединяем переведённые части
        translated_text = " ".join(translated_chunks)
        
        # Восстанавливаем элементы разметки
        translated_text = restore_preserved_elements(translated_text, placeholders)
        
        return translated_text
        
    except Exception as e:
        logger.error(f"Ошибка AI перевода: {e}")
        return text

def process_markdown_file(src_path: str, dest_path: str, model, tokenizer, 
                         glossary: Dict[str, str], config: TranslationConfig,
                         monitor: ResourceMonitor) -> bool:
    """Обработка Markdown файла с мониторингом ресурсов"""
    try:
        # Проверка размера файла
        file_size = os.path.getsize(src_path)
        max_size = config.get('limits', 'max_file_size_bytes') or 1048576
        
        if file_size > max_size:
            logger.warning(f"Файл {src_path} превышает максимальный размер ({file_size} > {max_size} байт)")
            return False
        
        # Проверка памяти
        if not monitor.check_memory_usage():
            logger.warning(f"Пропускаем файл {src_path} из-за нехватки памяти")
            return False
        
        # Чтение файла
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Создание директории назначения
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Перевод
        timeout = config.get('limits', 'timeout_per_file_seconds') or 300
        
        if model and tokenizer:
            max_tokens = config.get('limits', 'max_tokens_per_input') or 512
            translated_content = translate_text_ai(content, model, tokenizer, glossary, max_tokens, timeout)
        else:
            translated_content = translate_text_simple(content, glossary)
        
        # Сохранение результата
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        logger.info(f"✓ Переведен: {Path(src_path).name} ({file_size} байт)")
        return True
        
    except Exception as e:
        logger.error(f"✗ Ошибка обработки файла {src_path}: {e}")
        return False

def process_image_file(src_path: str, dest_path: str, model=None, tokenizer=None, 
                      glossary: Optional[Dict[str, str]] = None, config: Optional[TranslationConfig] = None) -> bool:
    """Обработка изображения"""
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Если OCR недоступен, просто копируем
        if not HAS_OCR:
            copyfile(src_path, dest_path)
            logger.info(f"✓ Скопировано изображение: {Path(src_path).name}")
            return True
        
        # Проверка размера изображения
        if config:
            max_image_size = config.get('limits', 'max_image_size_bytes') or 10485760
            file_size = os.path.getsize(src_path)
            if file_size > max_image_size:
                logger.warning(f"Изображение {src_path} слишком большое ({file_size} > {max_image_size} байт)")
                copyfile(src_path, dest_path)
                return True
        
        # Извлечение текста
        original_text, image = extract_text_from_image(src_path)
        
        if not original_text or not image:
            copyfile(src_path, dest_path)
            logger.info(f"✓ Скопировано изображение (текст не найден): {Path(src_path).name}")
            return True
        
        # Ограничение длины текста
        max_text_length = config.get('limits', 'max_text_length_on_image') if config else 5000
        if max_text_length and len(original_text) > max_text_length:
            logger.info(f"Текст на изображении слишком длинный ({len(original_text)} > {max_text_length}), копируем оригинал")
            copyfile(src_path, dest_path)
            return True
        
        # Перевод текста
        if model and tokenizer:
            translated_text = translate_text_ai(original_text, model, tokenizer, glossary)
        else:
            translated_text = translate_text_simple(original_text, glossary)
        
        # Наложение перевода
        new_image = overlay_text_on_image(image, translated_text)
        
        if new_image:
            new_image.save(dest_path, quality=95, optimize=True)
            logger.info(f"✓ Обработано изображение с текстом: {Path(src_path).name}")
        else:
            copyfile(src_path, dest_path)
            logger.info(f"✓ Скопировано изображение: {Path(src_path).name}")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Ошибка обработки изображения {src_path}: {e}")
        return False

def extract_text_from_image(image_path: str, lang: str = 'rus') -> Tuple[str, Optional['Image.Image']]:
    """Извлечение текста с изображения с помощью Tesseract OCR"""
    if not HAS_OCR:
        logger.debug("OCR недоступен - возвращаем пустой текст")
        return "", None
    
    try:
        image = Image.open(image_path)
        # Конфигурация для лучшего распознавания
        config = '--oem 3 --psm 6 -c tessedit_char_whitelist=АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?;:()[]{}"\'-+= '
        text = pytesseract.image_to_string(image, lang=lang, config=config)
        return text.strip(), image
    except Exception as e:
        logger.error(f"Ошибка извлечения текста из {image_path}: {e}")
        return "", None

def overlay_text_on_image(image: 'Image.Image', translated_text: str) -> Optional['Image.Image']:
    """Наложение переведённого текста на изображение"""
    if not HAS_OCR:
        return image
    
    try:
        # Ограничение длины отображаемого текста
        if len(translated_text) > 500:
            translated_text = translated_text[:497] + "..."
        
        # Конвертируем изображение для работы с OpenCV
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        height, width = image_cv.shape[:2]
        
        # Создаем область для текста
        text_height = 100
        new_height = height + text_height
        new_image = np.ones((new_height, width, 3), dtype=np.uint8) * 255
        
        # Вставляем оригинальное изображение
        new_image[:height, :] = image_cv
        
        # Разбиваем текст на строки
        words = translated_text.split()
        lines = []
        current_line = ""
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        thickness = 1
        max_width = width - 20
        
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
                    # Если даже одно слово не помещается, разбиваем его
                    lines.append(word)
        
        if current_line:
            lines.append(current_line)
        
        # Ограничиваем количество строк
        lines = lines[:3]
        
        # Накладываем текст
        line_height = 20
        start_y = height + 25
        
        for i, line in enumerate(lines):
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

def should_process_file(src_path: str, dest_path: str, force: bool = False) -> bool:
    """Проверка, нужно ли обрабатывать файл"""
    if force:
        return True
    
    if not os.path.exists(dest_path):
        return True
    
    try:
        return os.path.getmtime(src_path) > os.path.getmtime(dest_path)
    except OSError:
        return True

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
        
        # Определяем устройство
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = model.to(device)
        
        logger.info(f"Модель загружена на {device.upper()}")
        return model, tokenizer
        
    except Exception as e:
        logger.error(f"Ошибка загрузки модели: {e}")
        return None, None

def collect_files_to_process(source_dir: str, max_files: int, force: bool = False, 
                           target_dir: str = None) -> List[Tuple[str, str]]:
    """Сбор файлов для обработки с ограничением количества"""
    files_to_process = []
    supported_extensions = {'.md', '.png', '.jpg', '.jpeg', '.gif', '.bmp'}
    
    # Рекурсивный обход директории
    for root, dirs, files in os.walk(source_dir):
        # Пропускаем скрытые директории
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.startswith('.') or file in ['Thumbs.db', '.DS_Store']:
                continue
            
            file_ext = Path(file).suffix.lower()
            if file_ext not in supported_extensions:
                continue
            
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, source_dir)
            dest_path = os.path.join(target_dir, rel_path) if target_dir else None
            
            # Проверяем, нужно ли обрабатывать файл
            if dest_path and should_process_file(src_path, dest_path, force):
                files_to_process.append((src_path, dest_path))
                
                # Прерываем, если достигли лимита
                if len(files_to_process) >= max_files:
                    logger.info(f"Достигнут лимит файлов: {max_files}")
                    break
        
        if len(files_to_process) >= max_files:
            break
    
    return files_to_process

def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(description='Translate documentation from Russian to English')
    parser.add_argument('--source_dir', default='./ru', help='Source directory with Russian content')
    parser.add_argument('--target_dir', default='./en', help='Target directory for English content')
    parser.add_argument('--glossary', help='Path to glossary JSON file')
    parser.add_argument('--config', help='Path to configuration JSON file')
    parser.add_argument('--force', action='store_true', help='Force reprocessing of all files')
    parser.add_argument('--no-ai', action='store_true', help='Disable AI translation')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--max-files', type=int, help='Maximum files to process (overrides config)')
    parser.add_argument('--max-chars', type=int, help='Maximum characters per translation chunk')
    parser.add_argument('--max-tokens', type=int, help='Maximum tokens per model input')
    parser.add_argument('--max-file-size', type=int, help='Maximum file size in bytes')
    
    args = parser.parse_args()
    
    # Настройка логирования
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Проверка исходной директории
    if not os.path.exists(args.source_dir):
        logger.error(f"Исходная директория не существует: {args.source_dir}")
        return False
    
    # Загрузка конфигурации
    config = TranslationConfig(args.config)
    
    # Переопределение параметров из командной строки
    if args.max_files is not None:
        if not config.config.get('limits'):
            config.config['limits'] = {}
        config.config['limits']['max_files_per_run'] = args.max_files
    
    if args.max_chars is not None:
        config.config['limits']['max_chars_per_chunk'] = args.max_chars
    
    if args.max_tokens is not None:
        config.config['limits']['max_tokens_per_input'] = args.max_tokens
    
    if args.max_file_size is not None:
        config.config['limits']['max_file_size_bytes'] = args.max_file_size
    
    # Получение лимитов
    max_files = config.get('limits', 'max_files_per_run') or 20
    memory_limit = config.get('limits', 'max_memory_usage_mb') or 2048
    
    logger.info(f"Максимум файлов за прогон: {max_files}")
    logger.info(f"Лимит памяти: {memory_limit}MB")
    
    # Инициализация мониторинга ресурсов
    monitor = ResourceMonitor(memory_limit)
    
    # Загрузка глоссария
    glossary = load_glossary(args.glossary)
    
    # Загрузка модели перевода
    model, tokenizer = None, None
    if not args.no_ai:
        model, tokenizer = load_translation_model()
        if model and tokenizer:
            max_tokens = config.get('limits', 'max_tokens_per_input') or 512
            max_chars = config.get('limits', 'max_chars_per_chunk') or 10000
            logger.info(f"AI перевод настроен: макс. {max_chars} символов, {max_tokens} токенов")
    
    # Сбор файлов для обработки
    files_to_process = collect_files_to_process(
        args.source_dir, 
        max_files, 
        args.force, 
        args.target_dir
    )
    
    if not files_to_process:
        logger.info("Нет файлов для обработки")
        return True
    
    logger.info(f"Найдено {len(files_to_process)} файлов для обработки")
    
    # Счетчики
    processed_count = 0
    error_count = 0
    start_time = time.time()
    
    try:
        for i, (src_path, dest_path) in enumerate(files_to_process):
            logger.debug(f"Обработка файла {i + 1}/{len(files_to_process)}: {Path(src_path).name}")
            
            # Периодическая очистка памяти
            if i > 0 and i % 5 == 0:
                monitor.cleanup()
                if not monitor.check_memory_usage():
                    logger.warning("Критическое использование памяти, останавливаем обработку")
                    break
            
            success = False
            file_ext = Path(src_path).suffix.lower()
            
            try:
                if file_ext == '.md':
                    success = process_markdown_file(src_path, dest_path, model, tokenizer, glossary, config, monitor)
                elif file_ext in {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}:
                    success = process_image_file(src_path, dest_path, model, tokenizer, glossary, config)
                else:
                    # Копируем остальные файлы
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    copyfile(src_path, dest_path)
                    logger.info(f"✓ Скопирован: {Path(src_path).name}")
                    success = True
                    
            except KeyboardInterrupt:
                logger.info("Прервано пользователем")
                break
            except Exception as e:
                logger.error(f"✗ Критическая ошибка при обработке {src_path}: {e}")
                success = False
            
            if success:
                processed_count += 1
            else:
                error_count += 1
            
            # Логируем прогресс каждые 5 файлов
            if (i + 1) % 5 == 0:
                elapsed_time = monitor.get_elapsed_time()
                logger.info(f"Прогресс: {i + 1}/{len(files_to_process)}, время: {elapsed_time:.1f}с")
    
    finally:
        # Финальная очистка
        monitor.cleanup()
    
    # Финальная статистика
    elapsed_time = monitor.get_elapsed_time()
    logger.info("=" * 50)
    logger.info("ИТОГОВАЯ СТАТИСТИКА:")
    logger.info(f"✓ Успешно обработано: {processed_count}")
    logger.info(f"✗ Ошибок: {error_count}")
    logger.info(f"⏱ Время выполнения: {elapsed_time:.1f} секунд")
    logger.info(f"📊 Лимит файлов: {max_files}")
    logger.info(f"🔧 Режим AI: {'включен' if model else 'выключен'}")
    
    if HAS_PSUTIL:
        try:
            process = psutil.Process()
            memory_mb = process.memory_info().rss / 1024 / 1024
            logger.info(f"💾 Использование памяти: {memory_mb:.1f}MB")
        except:
            pass
    
    logger.info("=" * 50)
    
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
