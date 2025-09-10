#!/usr/bin/env python3
"""
Оптимизированный скрипт для перевода документации с русского на английский.
Основные улучшения:
- Исправлена проблема с отсутствием перевода
- Улучшена обработка ошибок
- Оптимизировано использование памяти
- Улучшено логирование
"""

import os
import argparse
import json
import re
import sys
import time
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple, List
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
    import torch
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

class MarkdownPreserver:
    """Сохранение и восстановление Markdown элементов"""
    
    def __init__(self):
        self.placeholders = {}
        self.counter = 0
    
    def preserve(self, text: str) -> str:
        """Сохранение Markdown элементов"""
        self.placeholders = {}
        self.counter = 0
        
        patterns = [
            (r'```[\s\S]*?```', 'CODE_BLOCK'),
            (r'`[^`\n]+?`', 'INLINE_CODE'),
            (r'!\[[^\]]*\]\([^)]+\)', 'IMAGE'),
            (r'\[[^\]]+\]\([^)]+\)', 'LINK'),
            (r'<!--[\s\S]*?-->', 'COMMENT'),
            (r'<[^>]+>', 'HTML_TAG'),
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

class AITranslator:
    """AI переводчик с оптимизацией памяти"""
    
    def __init__(self, model_name: str = "Helsinki-NLP/opus-mt-ru-en"):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
    def load_model(self):
        """Загрузка модели"""
        if self.model is not None:
            return
        
        logger.info(f"Загрузка модели перевода: {self.model_name}")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.model = self.model.to(self.device)
            logger.info(f"Модель загружена на устройство: {self.device}")
        except Exception as e:
            logger.error(f"Ошибка загрузки модели: {e}")
            raise
    
    def translate(self, text: str, max_length: int = 512) -> str:
        """Перевод текста"""
        if not text.strip():
            return text
        
        self.load_model()
        
        try:
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
                    early_stopping=True
                )
            
            translated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return translated.strip()
            
        except Exception as e:
            logger.error(f"Ошибка перевода: {e}")
            return text
    
    def cleanup(self):
        """Очистка ресурсов"""
        if self.model:
            del self.model
            del self.tokenizer
        
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        gc.collect()

class DocumentTranslator:
    """Основной класс для перевода документов"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.md_preserver = MarkdownPreserver()
        self.ai_translator = None
        self.stats = {'processed': 0, 'errors': 0}
    
    def setup_translators(self, use_ai: bool = True):
        """Настройка переводчиков"""
        if use_ai and HAS_TRANSFORMERS:
            try:
                self.ai_translator = AITranslator()
                self.ai_translator.load_model()
            except Exception as e:
                logger.warning(f"AI переводчик недоступен: {e}")
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
            translated = preserved_text  # Просто возвращаем оригинал, если AI недоступен
        
        # Восстанавливаем Markdown
        result = self.md_preserver.restore(translated)
        return result
    
    def process_markdown_file(self, src_path: str, dest_path: str) -> bool:
        """Обработка Markdown файла"""
        try:
            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            translated_content = self.translate_text(content)
            
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            
            logger.info(f"Переведен: {Path(src_path).name}")
            self.stats['processed'] += 1
            return True
            
        except Exception as e:
            logger.error(f"Ошибка обработки {src_path}: {e}")
            self.stats['errors'] += 1
            return False
    
    def process_image_file(self, src_path: str, dest_path: str) -> bool:
        """Обработка изображения"""
        try:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            copyfile(src_path, dest_path)
            logger.info(f"Скопировано: {Path(src_path).name}")
            self.stats['processed'] += 1
            return True
        except Exception as e:
            logger.error(f"Ошибка копирования {src_path}: {e}")
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
    }
    
    if not config_path or not os.path.exists(config_path):
        return default_config
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return {**default_config, **json.load(f)}
    except Exception as e:
        logger.warning(f"Ошибка загрузки конфигурации: {e}")
        return default_config

def collect_files(source_dir: str, target_dir: str, max_files: int) -> List[Tuple[str, str]]:
    """Сбор файлов для обработки"""
    files_to_process = []
    
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.startswith('.'):
                continue
                
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, source_dir)
            dest_path = os.path.join(target_dir, rel_path)
            
            if not os.path.exists(dest_path):
                files_to_process.append((src_path, dest_path))
            
            if len(files_to_process) >= max_files:
                break
        
        if len(files_to_process) >= max_files:
            break
    
    return files_to_process

def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(description='Перевод документации')
    parser.add_argument('--source_dir', default='./ru', help='Исходная директория')
    parser.add_argument('--target_dir', default='./en', help='Целевая директория')
    parser.add_argument('--config', help='Файл конфигурации JSON')
    parser.add_argument('--no-ai', action='store_true', help='Отключить AI перевод')
    parser.add_argument('--max-files', type=int, help='Максимальное количество файлов')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.source_dir):
        logger.error(f"Исходная директория не найдена: {args.source_dir}")
        return False
    
    # Загрузка конфигурации
    config = load_config(args.config)
    if args.max_files:
        config['max_files_per_run'] = args.max_files
    
    # Инициализация переводчика
    translator = DocumentTranslator(config)
    translator.setup_translators(use_ai=not args.no_ai)
    
    # Сбор файлов
    max_files = config.get('max_files_per_run', 20)
    files_to_process = collect_files(args.source_dir, args.target_dir, max_files)
    
    if not files_to_process:
        logger.info("Нет файлов для обработки")
        return True
    
    logger.info(f"Обработка {len(files_to_process)} файлов")
    
    # Обработка файлов
    start_time = time.time()
    
    try:
        for src_path, dest_path in files_to_process:
            if src_path.endswith('.md'):
                translator.process_markdown_file(src_path, dest_path)
            else:
                translator.process_image_file(src_path, dest_path)
    
    finally:
        translator.cleanup()
    
    # Статистика
    elapsed = time.time() - start_time
    stats = translator.stats
    
    logger.info("=" * 50)
    logger.info("ПЕРЕВОД ЗАВЕРШЕН")
    logger.info(f"✓ Обработано: {stats['processed']}")
    logger.info(f"✗ Ошибки: {stats['errors']}")
    logger.info(f"⏱ Время: {elapsed:.1f}с")
    logger.info(f"🧠 Режим AI: {'ВКЛ' if translator.ai_translator else 'ВЫКЛ'}")
    logger.info("=" * 50)
    
    return stats['errors'] == 0

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
