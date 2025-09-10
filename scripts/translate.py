#!/usr/bin/env python3
"""
Исправленный скрипт для перевода документации с русского на английский.
Основные улучшения:
- Корректная работа с Markdown элементами
- Упрощенная архитектура
- Надежная обработка ошибок
- Эффективное управление ресурсами
"""

import os
import argparse
import json
import re
import sys
import time
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple, List, Set
from shutil import copyfile
import gc

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Опциональные импорты
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

try:
    import torch
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

try:
    from PIL import Image
    import pytesseract
    HAS_OCR = True
except ImportError:
    HAS_OCR = False


class MarkdownPreserver:
    """Надежное сохранение и восстановление Markdown элементов"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.placeholders = {}
        self.counter = 0
    
    def preserve(self, text: str) -> str:
        """Сохранение Markdown элементов с уникальными плейсхолдерами"""
        self.reset()
        
        # Упорядоченные паттерны - от самых специфичных к общим
        patterns = [
            # Блоки кода (самый приоритетный)
            (r'```[\s\S]*?```', 'CODE_BLOCK'),
            # Инлайн код
            (r'`[^`\n]+?`', 'INLINE_CODE'),
            # Изображения
            (r'!\[[^\]]*\]\([^)]+\)', 'IMAGE'),
            # Ссылки
            (r'\[[^\]]+\]\([^)]+\)', 'LINK'),
            # HTML комментарии
            (r'<!--[\s\S]*?-->', 'COMMENT'),
            # HTML теги
            (r'<[^>]+>', 'HTML_TAG'),
            # Математические блоки
            (r'\$\$[\s\S]*?\$\$', 'MATH_BLOCK'),
            (r'\$[^$\n]+?\$', 'MATH_INLINE'),
            # Заголовки
            (r'^#{1,6}\s+.+$', 'HEADER'),
            # Строки таблиц
            (r'^\|.+\|$', 'TABLE_ROW'),
        ]
        
        for pattern, element_type in patterns:
            def replace_func(match):
                placeholder = f'__MD_{element_type}_{self.counter}__'
                self.placeholders[placeholder] = match.group(0)
                self.counter += 1
                return placeholder
            
            text = re.sub(pattern, replace_func, text, flags=re.MULTILINE)
        
        return text
    
    def restore(self, text: str) -> str:
        """Восстановление сохраненных элементов"""
        for placeholder, original in self.placeholders.items():
            text = text.replace(placeholder, original)
        return text
    
    def validate_restoration(self, original: str, translated: str) -> bool:
        """Проверка качества восстановления"""
        # Подсчет плейсхолдеров
        placeholder_pattern = r'__MD_\w+_\d+__'
        original_count = len(re.findall(placeholder_pattern, original))
        translated_count = len(re.findall(placeholder_pattern, translated))
        
        # Если количество не совпадает, плейсхолдеры повреждены
        if original_count != translated_count:
            logger.warning(f"Placeholder mismatch: {original_count} -> {translated_count}")
            return False
        
        return True


class SimpleTranslator:
    """Упрощенный переводчик с глоссарием"""
    
    def __init__(self, glossary: Dict[str, str] = None):
        self.glossary = glossary or {}
    
    def translate(self, text: str) -> str:
        """Простой перевод через глоссарий"""
        if not text.strip():
            return text
        
        result = text
        for ru_term, en_term in self.glossary.items():
            # Точное совпадение слов
            pattern = r'\b' + re.escape(ru_term) + r'\b'
            result = re.sub(pattern, en_term, result, flags=re.IGNORECASE)
        
        return result


class AITranslator:
    """AI переводчик с оптимизацией"""
    
    def __init__(self, model_name: str = "Helsinki-NLP/opus-mt-ru-en"):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.glossary = {}
        
    def load_model(self):
        """Загрузка модели один раз"""
        if self.model is not None:
            return
        
        logger.info(f"Loading translation model: {self.model_name}")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.model = self.model.to(self.device)
            logger.info(f"Model loaded on {self.device}")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
    
    def set_glossary(self, glossary: Dict[str, str]):
        """Установка глоссария"""
        self.glossary = glossary or {}
    
    def translate(self, text: str, max_length: int = 512) -> str:
        """Перевод текста с предварительной обработкой"""
        if not text.strip():
            return text
        
        self.load_model()
        
        # Применяем глоссарий до разбиения
        processed_text = self._apply_glossary(text)
        
        # Разбиваем на предложения для лучшего качества
        sentences = self._split_sentences(processed_text)
        translated_sentences = []
        
        for sentence in sentences:
            if not sentence.strip():
                translated_sentences.append(sentence)
                continue
            
            try:
                translated = self._translate_single(sentence, max_length)
                translated_sentences.append(translated)
            except Exception as e:
                logger.warning(f"Translation failed for sentence, keeping original: {e}")
                translated_sentences.append(sentence)
        
        return ' '.join(translated_sentences)
    
    def _apply_glossary(self, text: str) -> str:
        """Применение глоссария"""
        result = text
        for ru_term, en_term in self.glossary.items():
            pattern = r'\b' + re.escape(ru_term) + r'\b'
            result = re.sub(pattern, en_term, result, flags=re.IGNORECASE)
        return result
    
    def _split_sentences(self, text: str) -> List[str]:
        """Разбиение на предложения"""
        # Простое разбиение по знакам препинания
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _translate_single(self, text: str, max_length: int) -> str:
        """Перевод одного фрагмента"""
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length
        ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                num_beams=2,
                early_stopping=True,
                do_sample=False
            )
        
        translated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated.strip()
    
    def cleanup(self):
        """Очистка ресурсов"""
        if self.model:
            del self.model
            del self.tokenizer
            self.model = None
            self.tokenizer = None
        
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        gc.collect()


class DocumentTranslator:
    """Основной класс для перевода документов"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.md_preserver = MarkdownPreserver()
        self.simple_translator = None
        self.ai_translator = None
        self.stats = {
            'processed': 0,
            'errors': 0,
            'skipped': 0
        }
    
    def setup_translators(self, glossary: Dict[str, str], use_ai: bool = True):
        """Настройка переводчиков"""
        self.simple_translator = SimpleTranslator(glossary)
        
        if use_ai and HAS_TRANSFORMERS:
            try:
                self.ai_translator = AITranslator()
                self.ai_translator.set_glossary(glossary)
                self.ai_translator.load_model()
            except Exception as e:
                logger.warning(f"AI translator setup failed: {e}")
                self.ai_translator = None
    
    def translate_text(self, text: str) -> str:
        """Перевод текста с сохранением Markdown"""
        if not text.strip():
            return text
        
        # Сохраняем Markdown элементы
        preserved_text = self.md_preserver.preserve(text)
        
        # Переводим
        if self.ai_translator:
            max_tokens = self.config.get('max_tokens', 512)
            translated = self.ai_translator.translate(preserved_text, max_tokens)
        else:
            translated = self.simple_translator.translate(preserved_text)
        
        # Проверяем качество сохранения
        if not self.md_preserver.validate_restoration(preserved_text, translated):
            logger.warning("Markdown elements corrupted, using original")
            return text
        
        # Восстанавливаем Markdown
        result = self.md_preserver.restore(translated)
        return result
    
    def process_markdown_file(self, src_path: str, dest_path: str) -> bool:
        """Обработка Markdown файла"""
        try:
            # Проверка размера
            file_size = os.path.getsize(src_path)
            max_size = self.config.get('max_file_size', 1048576)
            
            if file_size > max_size:
                logger.warning(f"File too large: {src_path} ({file_size} bytes)")
                return False
            
            # Чтение
            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Перевод
            translated_content = self.translate_text(content)
            
            # Создание директории и сохранение
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            
            logger.info(f"✓ Translated: {Path(src_path).name}")
            self.stats['processed'] += 1
            return True
            
        except Exception as e:
            logger.error(f"✗ Failed to process {src_path}: {e}")
            self.stats['errors'] += 1
            return False
    
    def process_image_file(self, src_path: str, dest_path: str) -> bool:
        """Обработка изображения (пока просто копирование)"""
        try:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            copyfile(src_path, dest_path)
            logger.info(f"✓ Copied: {Path(src_path).name}")
            self.stats['processed'] += 1
            return True
        except Exception as e:
            logger.error(f"✗ Failed to copy {src_path}: {e}")
            self.stats['errors'] += 1
            return False
    
    def cleanup(self):
        """Очистка ресурсов"""
        if self.ai_translator:
            self.ai_translator.cleanup()


def load_config(config_path: str) -> Dict:
    """Загрузка конфигурации"""
    default_config = {
        'max_files_per_run': 20,
        'max_tokens': 512,
        'max_file_size': 1048576,
        'timeout_seconds': 300
    }
    
    if not config_path or not os.path.exists(config_path):
        return default_config
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            file_config = json.load(f)
        
        # Объединяем конфигурации
        config = default_config.copy()
        if 'limits' in file_config:
            config.update(file_config['limits'])
        
        return config
    except Exception as e:
        logger.warning(f"Config load failed: {e}")
        return default_config


def load_glossary(glossary_path: str) -> Dict[str, str]:
    """Загрузка глоссария"""
    if not glossary_path or not os.path.exists(glossary_path):
        return {}
    
    try:
        with open(glossary_path, 'r', encoding='utf-8') as f:
            glossary = json.load(f)
        logger.info(f"Loaded glossary with {len(glossary)} terms")
        return glossary
    except Exception as e:
        logger.error(f"Glossary load failed: {e}")
        return {}


def collect_files(source_dir: str, target_dir: str, max_files: int, 
                 force: bool = False) -> List[Tuple[str, str]]:
    """Сбор файлов для обработки"""
    files_to_process = []
    supported_extensions = {'.md', '.png', '.jpg', '.jpeg'}
    
    for root, dirs, files in os.walk(source_dir):
        # Пропускаем скрытые директории
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.startswith('.'):
                continue
                
            file_ext = Path(file).suffix.lower()
            if file_ext not in supported_extensions:
                continue
            
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, source_dir)
            dest_path = os.path.join(target_dir, rel_path)
            
            # Проверяем, нужно ли обрабатывать
            if force or not os.path.exists(dest_path) or \
               os.path.getmtime(src_path) > os.path.getmtime(dest_path):
                files_to_process.append((src_path, dest_path))
            
            if len(files_to_process) >= max_files:
                break
        
        if len(files_to_process) >= max_files:
            break
    
    return files_to_process


def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(description='Translate documentation')
    parser.add_argument('--source_dir', default='./ru', 
                       help='Source directory')
    parser.add_argument('--target_dir', default='./en', 
                       help='Target directory')
    parser.add_argument('--glossary', help='Glossary JSON file')
    parser.add_argument('--config', help='Config JSON file')
    parser.add_argument('--force', action='store_true', 
                       help='Force reprocessing')
    parser.add_argument('--no-ai', action='store_true', 
                       help='Disable AI translation')
    parser.add_argument('--max-files', type=int, 
                       help='Max files to process')
    parser.add_argument('--verbose', '-v', action='store_true')
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Проверка исходной директории
    if not os.path.exists(args.source_dir):
        logger.error(f"Source directory not found: {args.source_dir}")
        return False
    
    # Загрузка конфигурации
    config = load_config(args.config)
    if args.max_files:
        config['max_files_per_run'] = args.max_files
    
    # Загрузка глоссария
    glossary = load_glossary(args.glossary)
    
    # Инициализация переводчика
    translator = DocumentTranslator(config)
    translator.setup_translators(glossary, use_ai=not args.no_ai)
    
    # Сбор файлов
    max_files = config.get('max_files_per_run', 20)
    files_to_process = collect_files(
        args.source_dir, 
        args.target_dir, 
        max_files, 
        args.force
    )
    
    if not files_to_process:
        logger.info("No files to process")
        return True
    
    logger.info(f"Processing {len(files_to_process)} files")
    
    # Обработка файлов
    start_time = time.time()
    
    try:
        for src_path, dest_path in files_to_process:
            file_ext = Path(src_path).suffix.lower()
            
            if file_ext == '.md':
                translator.process_markdown_file(src_path, dest_path)
            else:
                translator.process_image_file(src_path, dest_path)
    
    finally:
        translator.cleanup()
    
    # Статистика
    elapsed = time.time() - start_time
    stats = translator.stats
    
    logger.info("=" * 50)
    logger.info("TRANSLATION COMPLETED")
    logger.info(f"✓ Processed: {stats['processed']}")
    logger.info(f"✗ Errors: {stats['errors']}")
    logger.info(f"⏱ Time: {elapsed:.1f}s")
    logger.info(f"🧠 AI Mode: {'ON' if translator.ai_translator else 'OFF'}")
    logger.info("=" * 50)
    
    return stats['errors'] == 0


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Critical error: {e}")
        sys.exit(1)
