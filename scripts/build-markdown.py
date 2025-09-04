#!/usr/bin/env python3
"""
Скрипт для сборки английской документации из переведенных JSON файлов
Восстанавливает markdown файлы с переведенным контентом
"""

import os
import json
import yaml
import frontmatter
import re
from pathlib import Path


def load_translations():
    """Загружает переведенные строки"""
    
    translations = {}
    
    # Пытаемся загрузить JSON
    json_path = Path('translations/en/documentation.json')
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            translations.update(json.load(f))
        print(f"📥 Loaded {len(translations)} translations from JSON")
    
    # Пытаемся загрузить YAML как дополнение
    yaml_path = Path('translations/en/docs-content.yml')
    if yaml_path.exists():
        with open(yaml_path, 'r', encoding='utf-8') as f:
            yaml_translations = yaml.safe_load(f)
            translations.update(yaml_translations)
        print(f"📥 Loaded additional translations from YAML")
    
    return translations


def load_file_structure():
    """Загружает структуру исходных файлов"""
    
    structure_path = Path('translations/files-structure.json')
    if not structure_path.exists():
        print("❌ File structure not found! Run extract-content.py first.")
        return {}
    
    with open(structure_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def rebuild_markdown_file(original_file, translations, file_structure):
    """Восстанавливает markdown файл с переведенным контентом"""
    
    # Читаем оригинальный файл
    with open(original_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Парсим frontmatter
    post = frontmatter.loads(content)
    
    # Получаем ключ файла
    relative_path = Path(original_file).relative_to('ru')
    file_key = str(relative_path).replace('/', '_').replace('.md', '')
    
    # Переводим frontmatter
    translated_frontmatter = post.metadata.copy()
    frontmatter_fields = ['title', 'description', 'summary', 'excerpt']
    
    for field in frontmatter_fields:
        if field in translated_frontmatter:
            translation_key = f"{file_key}_frontmatter_{field}"
            if translation_key in translations:
                translated_frontmatter[field] = translations[translation_key]
                print(f"  📝 Translated {field}: {translations[translation_key][:50]}...")
    
    # Переводим контент
    translated_content = translate_content_blocks(post.content, file_key, translations)
    
    # Создаем новый markdown файл
    new_post = frontmatter.Post(translated_content, **translated_frontmatter)
    
    return frontmatter.dumps(new_post)


def translate_content_blocks(content, file_key, translations):
    """Переводит блоки контента"""
    
    # Разбиваем контент на блоки аналогично extract-content.py
    sections = re.split(r'(^#{1,6}\s+.*$)', content, flags=re.MULTILINE)
    
    translated_sections = []
    block_id = 0
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
        
        if re.match(r'^#{1,6}\s+', section):
            # Заголовок
            translation_key = f"{file_key}_block_{block_id}"
            if translation_key in translations:
                translated_sections.append(translations[translation_key])
                print(f"  📍 Translated heading: {translations[translation_key]}")
            else:
                translated_sections.append(section)
            block_id += 1
        else:
            # Обычный контент - разбиваем на абзацы
            paragraphs = [p.strip() for p in section.split('\n\n') if p.strip()]
            translated_paragraphs = []
            
            for paragraph in paragraphs:
                translation_key = f"{file_key}_block_{block_id}"
                
                # Проверяем, что это переводимый блок
                if (not paragraph.startswith('```') and 
                    not paragraph.startswith('    ') and 
                    not re.match(r'^!\[.*\]\(.*\)$', paragraph.strip())):
                    
                    if translation_key in translations:
                        translated_paragraph = translations[translation_key]
                        # Обновляем ссылки на изображения в переведенном тексте
                        translated_paragraph = update_
