#!/usr/bin/env python3
"""
Основной скрипт для перевода документации.
Обрабатывает .md файлы и .png изображения.
"""

import os
import argparse
import json
import re
import torch
from pathlib import Path
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from PIL import Image
import pytesseract
from shutil import copyfile

def load_glossary(glossary_path):
    """Загрузка глоссария для специальных терминов"""
    if not glossary_path or not os.path.exists(glossary_path):
        return {}
    
    try:
        with open(glossary_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка загрузки глоссария: {e}")
        return {}

def translate_text(text, model, tokenizer, glossary=None, max_length=4096):
    """Перевод текста с учетом глоссария и сохранением форматирования"""
    if not text.strip():
        return text
    
    # Применяем глоссарий
    if glossary:
        for term, translation in glossary.items():
            text = re.sub(r'\b' + re.escape(term) + r'\b', translation, text, flags=re.IGNORECASE)
    
    # Сохраняем блоки кода, ссылки и специальные форматы от перевода
    placeholders = {}
    patterns = [
        r'(```.*?```)',  # Блоки кода
        r'(`.*?`)',      # Встроенный код
        r'(\[.*?\]\(.*?\))',  # Ссылки
        r'(<!--.*?-->)',  # HTML комментарии
        r'(<[^>]+>)',     # HTML теги
    ]
    
    combined_pattern = '|'.join(patterns)
    parts = re.split(combined_pattern, text, flags=re.DOTALL)
    
    for i, part in enumerate(parts):
        if part and re.match(combined_pattern, part, flags=re.DOTALL):
            placeholder = f'__PLACEHOLDER_{i}__'
            placeholders[placeholder] = part
            parts[i] = placeholder
    
    text_to_translate = ''.join(parts)
    
    # Пропускаем перевод, если нечего переводить
    if not text_to_translate.strip():
        return text
    
    try:
        # Для моделей перевода используем прямое кодирование текста
        inputs = tokenizer(
            text_to_translate, 
            return_tensors="pt", 
            padding=True, 
            truncation=True,
            max_length=max_length
        ).to(model.device)
        
        # Генерация перевода
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_length,
            num_beams=5,
            early_stopping=True
        )
        
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Восстанавливаем сохраненные элементы
        for placeholder, original in placeholders.items():
            translated_text = translated_text.replace(placeholder, original)
        
        return translated_text
    
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text  # Возвращаем оригинальный текст в случае ошибки

def process_markdown_file(src_path, dest_path, model, tokenizer, glossary):
    """Обработка Markdown файла"""
    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translated_content = translate_text(content, model, tokenizer, glossary)
        
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"✓ Переведен: {src_path} -> {dest_path}")
        return True
        
    except Exception as e:
        print(f"✗ Ошибка обработки файла {src_path}: {e}")
        return False

def process_image_file(src_path, dest_path):
    """Обработка изображения (пока просто копирование)"""
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        copyfile(src_path, dest_path)
        print(f"✓ Скопировано изображение: {src_path} -> {dest_path}")
        return True
        
    except Exception as e:
        print(f"✗ Ошибка копирования изображения {src_path}: {e}")
        return False

def should_process_file(src_path, dest_path):
    """Проверка, нужно ли обрабатывать файл"""
    if not os.path.exists(dest_path):
        return True
    
    # Обрабатываем, если исходный файл новее целевого
    return os.path.getmtime(src_path) > os.path.getmtime(dest_path)

def main(source_dir, target_dir, glossary_path=None):
    """Основная функция"""
    # Проверяем существование исходной директории
    if not os.path.exists(source_dir):
        print(f"✗ Исходная директория не существует: {source_dir}")
        return False
    
    glossary = load_glossary(glossary_path)
    
    # Инициализация модели перевода
    model_name = "Helsinki-NLP/opus-mt-ru-en"
    print(f"Загрузка модели {model_name}...")
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Перемещаем модель на GPU, если доступен
        if torch.cuda.is_available():
            model = model.to("cuda")
            print("Модель загружена на GPU")
        else:
            print("Модель загружена на CPU")
            
    except Exception as e:
        print(f"✗ Ошибка загрузки модели: {e}")
        return False
    
    processed_count = 0
    error_count = 0
    
    # Рекурсивный обход исходной директории
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, source_dir)
            dest_path = os.path.join(target_dir, rel_path)
            
            # Пропускаем скрытые файлы и системные файлы
            if file.startswith('.') or file in ['Thumbs.db', '.DS_Store']:
                continue
            
            # Обрабатываем только нужные файлы
            if file.endswith('.md'):
                if should_process_file(src_path, dest_path):
                    if process_markdown_file(src_path, dest_path, model, tokenizer, glossary):
                        processed_count += 1
                    else:
                        error_count += 1
            
            elif file.endswith('.png') and '.gitbook/assets' in root:
                if should_process_file(src_path, dest_path):
                    if process_image_file(src_path, dest_path):
                        processed_count += 1
                    else:
                        error_count += 1
    
    print(f"Обработка завершена. Успешно: {processed_count}, Ошибок: {error_count}")
    return error_count == 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate documentation from Russian to English')
    parser.add_argument('--source_dir', default='./ru', help='Source directory with Russian content')
    parser.add_argument('--target_dir', default='./en', help='Target directory for English content')
    parser.add_argument('--glossary', help='Path to glossary JSON file')
    
    args = parser.parse_args()
    
    success = main(args.source_dir, args.target_dir, args.glossary)
    exit(0 if success else 1)
