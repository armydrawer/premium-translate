#!/usr/bin/env python3
"""
Скрипт для извлечения переводимого контента из markdown файлов
Создает JSON/YAML файлы для перевода через SimpleLocalize
"""

import os
import json
import yaml
import frontmatter
import re
from pathlib import Path


def extract_translatable_content(markdown_content, file_path):
    """Извлекает переводимый контент из markdown файла"""
    
    # Парсим frontmatter
    post = frontmatter.loads(markdown_content)
    
    translatable_data = {
        'file_path': file_path,
        'frontmatter': {},
        'content_blocks': []
    }
    
    # Извлекаем переводимые поля из frontmatter
    frontmatter_fields = ['title', 'description', 'summary', 'excerpt']
    for field in frontmatter_fields:
        if field in post.metadata:
            translatable_data['frontmatter'][field] = post.metadata[field]
    
    # Разбиваем контент на блоки для перевода
    content = post.content
    
    # Разделяем по заголовкам
    sections = re.split(r'(^#{1,6}\s+.*$)', content, flags=re.MULTILINE)
    
    block_id = 0
    current_heading = None
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        # Проверяем, является ли это заголовком
        if re.match(r'^#{1,6}\s+', section):
            current_heading = section
            translatable_data['content_blocks'].append({
                'id': f'block_{block_id}',
                'type': 'heading',
                'content': section,
                'context': file_path
            })
            block_id += 1
        else:
            # Разбиваем обычный контент на абзацы
            paragraphs = [p.strip() for p in section.split('\n\n') if p.strip()]
            
            for paragraph in paragraphs:
                # Пропускаем блоки кода
                if paragraph.startswith('```') or paragraph.startswith('    '):
                    translatable_data['content_blocks'].append({
                        'id': f'block_{block_id}',
                        'type': 'code',
                        'content': paragraph,
                        'translate': False,
                        'context': f"{file_path} - {current_heading or 'root'}"
                    })
                # Пропускаем ссылки на изображения (их обработаем отдельно)
                elif re.match(r'^!\[.*\]\(.*\)$', paragraph.strip()):
                    translatable_data['content_blocks'].append({
                        'id': f'block_{block_id}',
                        'type': 'image',
                        'content': paragraph,
                        'translate': False,
                        'context': f"{file_path} - {current_heading or 'root'}"
                    })
                else:
                    # Обычный текст для перевода
                    translatable_data['content_blocks'].append({
                        'id': f'block_{block_id}',
                        'type': 'text',
                        'content': paragraph,
                        'translate': True,
                        'context': f"{file_path} - {current_heading or 'root'}"
                    })
                
                block_id += 1
    
    return translatable_data


def process_ru_files():
    """Обрабатывает все markdown файлы в папке ru/"""
    
    ru_path = Path('ru')
    translations_path = Path('translations')
    translations_path.mkdir(exist_ok=True)
    
    all_translations = {}
    files_structure = {}
    
    # Обходим все .md файлы в папке ru/
    for md_file in ru_path.rglob('*.md'):
        relative_path = str(md_file.relative_to(ru_path))
        print(f"📄 Processing: {relative_path}")
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Извлекаем переводимый контент
            translatable = extract_translatable_content(content, relative_path)
            
            # Сохраняем структуру файла
            files_structure[relative_path] = {
                'blocks_count': len(translatable['content_blocks']),
                'has_frontmatter': bool(translatable['frontmatter']),
                'original_file': str(md_file)
            }
            
            # Создаем ключи для перевода
            file_key = relative_path.replace('/', '_').replace('.md', '')
            
            # Frontmatter
            if translatable['frontmatter']:
                for field, value in translatable['frontmatter'].items():
                    key = f"{file_key}_frontmatter_{field}"
                    all_translations[key] = value
            
            # Контентные блоки
            for block in translatable['content_blocks']:
                if block.get('translate', True):
                    key = f"{file_key}_{block['id']}"
                    all_translations[key] = block['content']
                    
        except Exception as e:
            print(f"❌ Error processing {md_file}: {e}")
            continue
    
    # Сохраняем JSON для SimpleLocalize
    json_path = translations_path / 'ru' / 'documentation.json'
    json_path.parent.mkdir(exist_ok=True)
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Saved {len(all_translations)} translation keys to {json_path}")
    
    # Сохраняем YAML как альтернативу
    yaml_path = translations_path / 'ru' / 'docs-content.yml'
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(all_translations, f, allow_unicode=True, default_flow_style=False)
    
    print(f"✅ Saved YAML version to {yaml_path}")
    
    # Сохраняем структуру файлов для последующей сборки
    structure_path = translations_path / 'files-structure.json'
    with open(structure_path, 'w', encoding='utf-8') as f:
        json.dump(files_structure, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Saved file structure to {structure_path}")
    
    return len(all_translations)


if __name__ == '__main__':
    print("🔄 Extracting translatable content from Russian documentation...")
    
    if not Path('ru').exists():
        print("❌ Directory 'ru' not found!")
        exit(1)
    
    keys_count = process_ru_files()
    print(f"🎯 Extraction complete! {keys_count} translation keys prepared.")
    print("📤 Files are ready for SimpleLocalize processing.")
