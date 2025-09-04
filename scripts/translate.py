#!/usr/bin/env python3
"""
Основной скрипт для перевода документации.
Обрабатывает .md файлы и .png изображения.
"""

import os
import argparse
import json
import re
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import pytesseract
from image_processor import process_image

def load_glossary(glossary_path):
    """Загрузка глоссария для специальных терминов"""
    if glossary_path and os.path.exists(glossary_path):
        with open(glossary_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def translate_text(text, model, tokenizer, glossary=None):
    """Перевод текста с учетом глоссария и сохранением форматирования"""
    if glossary:
        for term, translation in glossary.items():
            text = re.sub(r'\b' + re.escape(term) + r'\b', translation, text, flags=re.IGNORECASE)
    
    # Сохраняем блоки кода и ссылки от перевода
    placeholders = {}
    parts = re.split(r'(```.*?```|`.*?`|\[.*?\]\(.*?\))', text, flags=re.DOTALL)
    
    for i, part in enumerate(parts):
        if re.match(r'(```.*?```|`.*?`|\[.*?\]\(.*?\))', part, flags=re.DOTALL):
            placeholder = f'__PLACEHOLDER_{i}__'
            placeholders[placeholder] = part
            parts[i] = placeholder
    
    text_to_translate = ''.join(parts)
    
    # Подготовка промпта для перевода
    messages = [
        {
            "role": "system", 
            "content": "You are a professional technical translator. Translate Russian to English while preserving all Markdown formatting, code blocks, and links."
        },
        {
            "role": "user", 
            "content": f"Translate this technical documentation to English:\n\n{text_to_translate}"
        }
    ]
    
    inputs = tokenizer.apply_chat_template(
        messages, 
        return_tensors="pt"
    ).to(model.device)
    
    outputs = model.generate(
        inputs, 
        max_new_tokens=4096,
        temperature=0.3,
        do_sample=True
    )
    
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Восстанавливаем блоки кода и ссылки
    for placeholder, original in placeholders.items():
        translated_text = translated_text.replace(placeholder, original)
    
    return translated_text

def process_file(src_path, dest_path, model, tokenizer, glossary):
    """Обработка одного файла"""
    print(f"Processing: {src_path} -> {dest_path}")
    
    # Создаем целевую директорию, если не существует
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    if src_path.endswith('.md'):
        # Обработка Markdown файлов
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translated_content = translate_text(content, model, tokenizer, glossary)
        
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
            
    elif src_path.endswith('.png') and '.gitbook/assets' in src_path:
        # Обработка скриншотов
        process_image(src_path, dest_path, model, tokenizer, glossary)

def main(source_dir, target_dir, glossary_path=None):
    """Основная функция"""
    glossary = load_glossary(glossary_path)
    
    # Инициализация модели перевода
    model_name = "Helsinki-NLP/opus-mt-ru-en"  # Легкая модель для демонстрации
    print(f"Loading model {model_name}...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype="auto"
    )
    
    # Рекурсивный обход исходной директории
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if not (file.endswith('.md') or (file.endswith('.png') and '.gitbook/assets' in root)):
                continue
                
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, source_dir)
            dest_path = os.path.join(target_dir, rel_path)
            
            # Пропускаем, если целевой файл новее исходного
            if (os.path.exists(dest_path) and 
                os.path.getmtime(dest_path) >= os.path.getmtime(src_path)):
                continue
                
            process_file(src_path, dest_path, model, tokenizer, glossary)
    
    print("Translation completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate documentation from Russian to English')
    parser.add_argument('--source_dir', default='./ru', help='Source directory with Russian content')
    parser.add_argument('--target_dir', default='./en', help='Target directory for English content')
    parser.add_argument('--glossary', help='Path to glossary JSON file')
    
    args = parser.parse_args()
    main(args.source_dir, args.target_dir, args.glossary)
