#!/usr/bin/env python3

"""
Модуль для обработки и перевода текста на изображениях.
Исправленная версия с улучшенной обработкой ошибок и производительностью.
"""

import os
import logging
from typing import Optional, Tuple, List, Dict
from pathlib import Path

# Опциональные импорты для OCR
try:
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont, ImageEnhance
    import pytesseract
    HAS_OCR = True
except ImportError:
    HAS_OCR = False

logger = logging.getLogger(__name__)

class ImageTextProcessor:
    """Класс для обработки текста на изображениях с улучшенными возможностями"""

    def __init__(self, lang: str = 'rus', config: Optional[Dict] = None):
        self.lang = lang
        self.config = config or {}
        self.font_path = self._get_system_font()
        self.min_confidence = self.config.get('min_confidence', 30)
        self.max_text_lines = self.config.get('max_text_lines_on_image', 5)
        
        if not HAS_OCR:
            logger.warning("OCR библиотеки не установлены")

    def _get_system_font(self) -> Optional[str]:
        """Получение системного шрифта с расширенным поиском"""
        possible_fonts = [
            # Windows
            'C:/Windows/Fonts/arial.ttf',
            'C:/Windows/Fonts/calibri.ttf',
            'C:/Windows/Fonts/tahoma.ttf',
            # macOS
            '/System/Library/Fonts/Arial.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
            '/Library/Fonts/Arial.ttf',
            # Linux
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            '/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf',
            '/usr/share/fonts/TTF/arial.ttf',
            # Ubuntu/Debian альтернативы
            '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf',
        ]
        
        for font_path in possible_fonts:
            if os.path.exists(font_path):
                logger.debug(f"Найден системный шрифт: {font_path}")
                return font_path
        
        logger.warning("Системный шрифт не найден, будет использован шрифт по умолчанию")
        return None

    def extract_text(self, image_path: str) -> Tuple[str, Optional[Image.Image]]:
        """Извлечение текста с изображения с улучшенной предобработкой"""
        if not HAS_OCR:
            return "", None
        
        try:
            # Проверка существования файла
            if not os.path.exists(image_path):
                logger.error(f"Файл изображения не найден: {image_path}")
                return "", None
            
            # Проверка размера файла
            file_size = os.path.getsize(image_path)
            max_size = self.config.get('max_image_size_bytes', 10485760)  # 10MB
            if file_size > max_size:
                logger.warning(f"Изображение {image_path} слишком большое: {file_size} > {max_size} байт")
                return "", None
            
            # Загружаем изображение
            image = Image.open(image_path)
            
            # Конвертируем в RGB если нужно
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Предобработка изображения для лучшего распознавания
            processed_image = self._preprocess_image(image)
            
            # Конфигурация Tesseract для лучшего распознавания
            config = self._get_tesseract_config()
            
            # Извлекаем текст с несколькими попытками
            text = self._extract_text_with_retries(processed_image, config)
            
            return text.strip(), image
            
        except Exception as e:
            logger.error(f"Ошибка извлечения текста из {image_path}: {e}")
            return "", None

    def _get_tesseract_config(self) -> str:
        """Получение оптимальной конфигурации Tesseract"""
        whitelist = self.config.get('char_whitelist', 
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?;:()[]{}"\'-+= ')
        
        return f'--oem 3 --psm 6 -c tessedit_char_whitelist={whitelist}'

    def _extract_text_with_retries(self, image: Image.Image, config: str, max_retries: int = 3) -> str:
        """Извлечение текста с несколькими попытками и разными настройками"""
        texts = []
        
        # Основная попытка
        try:
            text = pytesseract.image_to_string(image, lang=self.lang, config=config)
            if text.strip():
                texts.append(text.strip())
        except Exception as e:
            logger.debug(f"Основная попытка OCR не удалась: {e}")
        
        # Попытка с другими PSM режимами
        psm_modes = [3, 4, 6, 7, 8]  # Разные режимы сегментации страницы
        
        for psm in psm_modes:
            if len(texts) >= max_retries:
                break
            
            try:
                config_alt = config.replace('--psm 6', f'--psm {psm}')
                text = pytesseract.image_to_string(image, lang=self.lang, config=config_alt)
                if text.strip() and text.strip() not in texts:
                    texts.append(text.strip())
            except Exception:
                continue
        
        # Возвращаем самый длинный результат
        if texts:
            return max(texts, key=len)
        
        return ""

    def _preprocess_image(self, image: Image.Image) -> Image.Image:
        """Улучшенная предобработка изображения для OCR"""
        try:
            # Конвертируем в numpy array
            img_array = np.array(image)
            
            # Конвертируем в оттенки серого
            if len(img_array.shape) == 3:
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            else:
                gray = img_array
            
            # Улучшение контрастности с помощью CLAHE
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            enhanced = clahe.apply(gray)
            
            # Удаление шума
            denoised = cv2.medianBlur(enhanced, 3)
            
            # Адаптивная бинаризация
            binary = cv2.adaptiveThreshold(
                denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                cv2.THRESH_BINARY, 11, 2
            )
            
            # Морфологические операции для улучшения текста
            kernel = np.ones((1, 1), np.uint8)
            processed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
            
            return Image.fromarray(processed)
            
        except Exception as e:
            logger.warning(f"Ошибка предобработки изображения: {e}")
            return image

    def detect_text_regions(self, image: Image.Image) -> List[Dict]:
        """Определение областей с текстом на изображении"""
        if not HAS_OCR:
            return []
        
        try:
            img_array = np.array(image)
            config = self._get_tesseract_config()
            
            data = pytesseract.image_to_data(
                img_array, 
                lang=self.lang, 
                config=config,
                output_type=pytesseract.Output.DICT
            )
            
            text_regions = []
            n_boxes = len(data['level'])
            
            for i in range(n_boxes):
                confidence = int(data['conf'][i])
                text = data['text'][i].strip()
                
                if confidence > self.min_confidence and text:
                    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                    
                    text_regions.append({
                        'text': text,
                        'bbox': (x, y, x + w, y + h),
                        'confidence': confidence
                    })
            
            # Сортируем по уверенности
            text_regions.sort(key=lambda x: x['confidence'], reverse=True)
            
            return text_regions
            
        except Exception as e:
            logger.error(f"Ошибка определения текстовых областей: {e}")
            return []

    def create_translated_image(self, original_image: Image.Image, original_text: str, 
                              translated_text: str, method: str = 'overlay') -> Image.Image:
        """Создание изображения с переведенным текстом"""
        if method == 'overlay':
            return self._overlay_translation(original_image, translated_text)
        elif method == 'replace':
            return self._replace_text_regions(original_image, original_text, translated_text)
        else:
            return self._overlay_translation(original_image, translated_text)

    def _overlay_translation(self, image: Image.Image, translated_text: str) -> Image.Image:
        """Улучшенное наложение перевода с форматированием"""
        if not translated_text.strip():
            return image
        
        try:
            # Ограничение длины текста
            max_display_length = self.config.get('max_display_text_length', 500)
            if len(translated_text) > max_display_length:
                translated_text = translated_text[:max_display_length-3] + "..."
            
            # Разбиваем текст на строки
            lines = self._wrap_text_smart(translated_text, image.width - 40)
            
            # Ограничиваем количество строк
            if len(lines) > self.max_text_lines:
                lines = lines[:self.max_text_lines-1] + [lines[self.max_text_lines-1][:47] + "..."]
            
            # Рассчитываем размеры
            line_height = 25
            padding = 20
            text_area_height = len(lines) * line_height + padding
            
            # Создаем новое изображение
            new_height = image.height + text_area_height
            new_image = Image.new('RGB', (image.width, new_height), 'white')
            new_image.paste(image, (0, 0))
            
            # Создаем полупрозрачную подложку
            overlay = Image.new('RGBA', (image.width, text_area_height), (255, 255, 255, 240))
            new_image.paste(overlay, (0, image.height), overlay)
            
            # Получаем шрифт
            font = self._get_font(size=14)
            
            # Рисуем текст
            draw = ImageDraw.Draw(new_image)
            y_offset = image.height + 10
            
            for line in lines:
                if y_offset + line_height > new_height - 5:
                    break
                
                # Центрируем текст если он короткий
                if len(line) < 50:
                    try:
                        text_width = draw.textlength(line, font=font)
                        x_offset = max(20, (image.width - text_width) // 2)
                    except AttributeError:
                        # Для старых версий Pillow
                        x_offset = 20
                else:
                    x_offset = 20
                
                draw.text((x_offset, y_offset), line, fill='black', font=font)
                y_offset += line_height
            
            return new_image
            
        except Exception as e:
            logger.error(f"Ошибка создания изображения с переводом: {e}")
            return image

    def _get_font(self, size: int = 14) -> ImageFont.ImageFont:
        """Получение шрифта с обработкой ошибок"""
        try:
            if self.font_path and os.path.exists(self.font_path):
                return ImageFont.truetype(self.font_path, size)
        except Exception as e:
            logger.debug(f"Не удалось загрузить TrueType шрифт: {e}")
        
        try:
            return ImageFont.load_default()
        except Exception:
            # Для совсем старых версий Pillow
            return ImageFont.load_default()

    def _replace_text_regions(self, image: Image.Image, original_text: str, translated_text: str) -> Image.Image:
        """Замена текстовых областей (продвинутая реализация)"""
        try:
            # Получаем области с текстом
            text_regions = self.detect_text_regions(image)
            
            if not text_regions:
                logger.info("Текстовые области не найдены, используется overlay")
                return self._overlay_translation(image, translated_text)
            
            # Создаем копию изображения для редактирования
            result_image = image.copy()
            draw = ImageDraw.Draw(result_image)
            font = self._get_font(size=12)
            
            # Заменяем каждую область
            for region in text_regions[:3]:  # Ограничиваем количество замен
                bbox = region['bbox']
                
                # Закрашиваем область белым
                draw.rectangle(bbox, fill='white')
                
                # Размещаем переведенный текст
                translated_part = translated_text[:50]  # Берем часть перевода
                
                # Подгоняем размер шрифта под область
                region_width = bbox[2] - bbox[0]
                region_height = bbox[3] - bbox[1]
                
                font_size = min(12, region_height - 2)
                if font_size < 8:
                    font_size = 8
                
                try:
                    small_font = self._get_font(font_size)
                except:
                    small_font = font
                
                # Рисуем текст
                draw.text(
                    (bbox[0] + 2, bbox[1] + 2), 
                    translated_part, 
                    fill='black', 
                    font=small_font
                )
            
            return result_image
            
        except Exception as e:
            logger.error(f"Ошибка замены текстовых областей: {e}")
            return self._overlay_translation(image, translated_text)

    def _wrap_text_smart(self, text: str, max_width: int, char_width: int = 8) -> List[str]:
        """Умное разбиение текста на строки с учетом слов"""
        words = text.split()
        lines = []
        current_line = ""
        max_chars = max(20, max_width // char_width)  # Минимум 20 символов
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            
            if len(test_line) <= max_chars:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                    current_line = word
                else:
                    # Разбиваем слишком длинное слово
                    while len(word) > max_chars:
                        lines.append(word[:max_chars-1] + "-")
                        word = word[max_chars-1:]
                    current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines

    def process_image(self, src_path: str, dest_path: str, translate_func, 
                     glossary: Optional[Dict] = None, method: str = 'overlay') -> bool:
        """Полная обработка изображения с переводом и улучшенной обработкой ошибок"""
        try:
            # Создаем директорию назначения
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            # Извлекаем текст
            original_text, image = self.extract_text(src_path)
            
            if not original_text or not image:
                # Если текст не найден, копируем оригинал
                try:
                    image_orig = Image.open(src_path)
                    image_orig.save(dest_path, quality=95, optimize=True)
                    logger.info(f"Текст не найден, скопирован оригинал: {Path(src_path).name}")
                    return True
                except Exception as e:
                    logger.error(f"Ошибка копирования изображения: {e}")
                    return False
            
            # Проверяем длину извлеченного текста
            max_text_length = self.config.get('max_text_length_on_image', 5000)
            if len(original_text) > max_text_length:
                logger.info(f"Текст слишком длинный ({len(original_text)} > {max_text_length}), копируем оригинал")
                image.save(dest_path, quality=95, optimize=True)
                return True
            
            logger.debug(f"Извлеченный текст: {original_text[:100]}...")
            
            # Переводим текст
            try:
                translated_text = translate_func(original_text, glossary)
                logger.debug(f"Переведенный текст: {translated_text[:100]}...")
            except Exception as e:
                logger.error(f"Ошибка перевода текста: {e}")
                translated_text = original_text  # Используем оригинал при ошибке
            
            # Создаем результирующее изображение
            try:
                result_image = self.create_translated_image(
                    image, original_text, translated_text, method
                )
                
                # Сохраняем с оптимизацией
                result_image.save(dest_path, quality=95, optimize=True)
                logger.info(f"✓ Обработано изображение: {Path(src_path).name}")
                return True
                
            except Exception as e:
                logger.error(f"Ошибка создания результирующего изображения: {e}")
                # Сохраняем оригинал при ошибке
                image.save(dest_path, quality=95, optimize=True)
                return True
            
        except Exception as e:
            logger.error(f"Ошибка обработки изображения {src_path}: {e}")
            return False

def process_screenshot(src_path: str, dest_path: str, translate_func, 
                      glossary: Optional[Dict] = None, lang: str = 'rus', 
                      config: Optional[Dict] = None) -> bool:
    """Удобная функция для обработки скриншотов с конфигурацией"""
    processor = ImageTextProcessor(lang, config)
    return processor.process_image(src_path, dest_path, translate_func, glossary)

# Функции для обратной совместимости с основным скриптом
def extract_text_from_image(image_path: str, lang: str = 'rus') -> Tuple[str, Optional['Image.Image']]:
    """Обратная совместимость с основным скриптом"""
    processor = ImageTextProcessor(lang)
    return processor.extract_text(image_path)

def overlay_text_on_image(image: 'Image.Image', translated_text: str) -> Optional['Image.Image']:
    """Обратная совместимость с основным скриптом"""
    processor = ImageTextProcessor()
    return processor._overlay_translation(image, translated_text)

# Вспомогательные функции для тестирования
def test_ocr_availability() -> bool:
    """Тестирование доступности OCR"""
    if not HAS_OCR:
        print("OCR библиотеки не установлены")
        return False
    
    try:
        # Создаем тестовое изображение
        test_image = Image.new('RGB', (200, 50), 'white')
        draw = ImageDraw.Draw(test_image)
        draw.text((10, 10), "Test", fill='black')
        
        # Пробуем распознать
        text = pytesseract.image_to_string(test_image)
        print(f"OCR тест успешен: '{text.strip()}'")
        return True
        
    except Exception as e:
        print(f"OCR тест не пройден: {e}")
        return False

if __name__ == "__main__":
    # Простое тестирование модуля
    print("Тестирование модуля обработки изображений...")
    print(f"OCR доступен: {HAS_OCR}")
    
    if HAS_OCR:
        test_ocr_availability()
    
    processor = ImageTextProcessor()
    print(f"Системный шрифт: {processor.font_path}")
    print("Модуль готов к использованию!")
