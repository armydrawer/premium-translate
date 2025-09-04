#!/usr/bin/env python3
"""
Скрипт для генерации отчета о переводе документации
"""

import json
import os
from pathlib import Path
from datetime import datetime


def count_words(text):
    """Подсчет слов в тексте"""
    return len(text.split())


def analyze_translations():
    """Анализирует переводы и создает отчет"""
    
    # Загружаем структуру файлов
    structure_path = Path('translations/files-structure.json')
    if not structure_path.exists():
        return None
    
    with open(structure_path, 'r', encoding='utf-8') as f:
        file_structure = json.load(f)
    
    # Загружаем русские переводы
    ru_translations = {}
    ru_json_path = Path('translations/ru/documentation.json')
    if ru_json_path.exists():
        with open(ru_json_path, 'r', encoding='utf-8') as f:
            ru_translations = json.load(f)
    
    # Загружаем английские переводы
    en_translations = {}
    en_json_path = Path('translations/en/documentation.json')
    if en_json_path.exists():
        with open(en_json_path, 'r', encoding='utf-8') as f:
            en_translations = json.load(f)
    
    # Анализ
    analysis = {
        'files_processed': len(file_structure),
        'total_blocks': sum(info['blocks_count'] for info in file_structure.values()),
        'ru_keys': len(ru_translations),
        'en_keys': len(en_translations),
        'translation_coverage': 0,
        'total_ru_words': 0,
        'total_en_words': 0,
        'files_details': [],
        'missing_translations': [],
        'timestamp': datetime.now().isoformat()
    }
    
    # Подсчет слов
    for key, text in ru_translations.items():
        analysis['total_ru_words'] += count_words(str(text))
    
    for key, text in en_translations.items():
        analysis['total_en_words'] += count_words(str(text))
    
    # Покрытие переводов
    if analysis['ru_keys'] > 0:
        analysis['translation_coverage'] = (analysis['en_keys'] / analysis['ru_keys']) * 100
    
    # Детали по файлам
    for file_path, info in file_structure.items():
        file_key = file_path.replace('/', '_').replace('.md', '')
        
        # Подсчитываем переводы для этого файла
        file_ru_keys = [k for k in ru_translations.keys() if k.startswith(file_key)]
        file_en_keys = [k for k in en_translations.keys() if k.startswith(file_key)]
        
        file_coverage = 0
        if file_ru_keys:
            file_coverage = (len(file_en_keys) / len(file_ru_keys)) * 100
        
        analysis['files_details'].append({
            'file': file_path,
            'blocks': info['blocks_count'],
            'ru_keys': len(file_ru_keys),
            'en_keys': len(file_en_keys),
            'coverage': file_coverage,
            'status': '✅ Complete' if file_coverage >= 100 else '🔄 Partial' if file_coverage > 0 else '❌ Missing'
        })
    
    # Недостающие переводы
    for key in ru_translations:
        if key not in en_translations:
            analysis['missing_translations'].append(key)
    
    return analysis


def generate_report():
    """Генерирует markdown отчет"""
    
    analysis = analyze_translations()
    
    if not analysis:
        return """# Translation Report

❌ **Error**: Could not generate report. Translation data not found.

Please ensure that:
1. `extract-content.py` has been run
2. SimpleLocalize has processed the translations
3. Translation files exist in `translations/` directory

Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    # Генерируем отчет
    report = f"""# 📊 Translation Report

Generated at: **{datetime.fromisoformat(analysis['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}**

## 🎯 Overall Statistics

| Metric | Value |
|--------|-------|
| **Files processed** | {analysis['files_processed']} |
| **Total content blocks** | {analysis['total_blocks']} |
| **Russian translation keys** | {analysis['ru_keys']} |
| **English translation keys** | {analysis['en_keys']} |
| **Translation coverage** | {analysis['translation_coverage']:.1f}% |
| **Russian words** | {analysis['total_ru_words']:,} |
| **English words** | {analysis['total_en_words']:,} |

## 📈 Translation Status

"""
    
    if analysis['translation_coverage'] >= 100:
        report += "🎉 **Excellent!** All content has been translated.\n\n"
    elif analysis['translation_coverage'] >= 90:
        report += "✅ **Very Good!** Most content has been translated.\n\n"
    elif analysis['translation_coverage'] >= 70:
        report += "🔄 **Good Progress!** Majority of content is translated.\n\n"
    elif analysis['translation_coverage'] >= 50:
        report += "⏳ **In Progress** - About half of the content is translated.\n\n"
    else:
        report += "🚨 **Needs Attention** - Translation is incomplete.\n\n"
    
    # Детали по файлам
    report += "## 📄 Files Details\n\n"
    report += "| File | Blocks | Coverage | Status |\n"
    report += "|------|--------|----------|--------|\n"
    
    for file_detail in analysis['files_details']:
        report += f"| `{file_detail['file']}` | {file_detail['blocks']} | {file_detail['coverage']:.1f}% | {file_detail['status']} |\n"
    
    # Недостающие переводы
    if analysis['missing_translations']:
        report += f"\n## ⚠️ Missing Translations ({len(analysis['missing_translations'])} keys)\n\n"
        
        if len(analysis['missing_translations']) <= 20:
            report += "The following translation keys are missing:\n\n"
            for key in analysis['missing_translations']:
                report += f"- `{key}`\n"
        else:
            report += f"❗ Too many missing translations to list individually ({len(analysis['missing_translations'])} total).\n"
            report += "This suggests that SimpleLocalize hasn't processed the translations yet.\n"
    
    # Следующие шаги
    report += "\n## 🚀 Next Steps\n\n"
    
    if analysis['translation_coverage'] < 100:
        report += """1. **Wait for SimpleLocalize processing** - Translation service may still be working
2. **Check SimpleLocalize dashboard** - Verify translation status
3. **Review translation quality** - Some keys might need manual attention
4. **Re-run the workflow** - If needed, trigger translation update
"""
    else:
        report += """1. **Review generated English files** - Check translation quality
2. **Update images and screenshots** - Copy and localize visual content  
3. **Test documentation links** - Ensure all references work correctly
4. **Manual polish** - Fine-tune technical terms and context
"""
    
    # Команды для исправления
    report += "\n## 🛠️ Troubleshooting Commands\n\n"
    report += """```bash
# Re-extract content from Russian files
python scripts/extract-content.py

# Rebuild English files from translations  
python scripts/build-markdown.py

# Check file structure
find ru -name "*.md" | wc -l  # Russian files
find en -name "*.md" | wc -l  # English files (after build)

# Validate translations
ls -la translations/ru/
ls -la translations/en/
```

---

*This report was generated automatically by the premium-translate workflow* 🤖
"""
    
    return report


if __name__ == '__main__':
    print("📊 Generating translation report...")
    
    report = generate_report()
    print(report)
