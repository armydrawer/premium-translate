#!/usr/bin/env python3
"""
Модуль для обработки и перевода текста на изображениях.
"""
import os
import logging
from typing import Optional, Tuple
from pathlib import Path

# Опциональные импорты для OCR
try:
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    import pytesseract
    HAS_OCR = True
except ImportError:
    HAS_OCR = False

logger = logging.getLogger(__name__)


class ImageTextProcessor:
    """Класс для обработки текста на изображениях"""
    
    def __init__(self, lang: str = 'rus'):
        self.lang = lang
        self.font_path = self._get_system_font()
        
        if not HAS_OCR:
            logger.warning("OCR библиотеки не установлены")
    
    def _get_system_font(self) -> Optional[str]:
        """Получение системного шрифта"""
        possible_fonts = [
            '/System/Library/Fonts/Arial.ttf',  # macOS
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
            'C:/Windows/Fonts/arial.ttf',  # Windows
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',  # Linux alternative
        ]
        
        for font_path in possible_fonts:
            if os.path.exists(font_path):
                return font_path
        
        return None
    
    def extract_text(self, image_path: str) -> Tuple[str, Optional[Image.Image]]:
        """Извлечение текста с изображения"""
        if not HAS_OCR:
            return "", None
            
        try:
            # Загружаем изображение
            image = Image.open(image_path)
            
            # Предобработка изображения для лучшего распознавания
            processed_image = self._preprocess_image(image)
            
            # Конфигурация Tesseract для лучшего распознавания
            config = '--oem 3 --psm 6 -c tessedit_char_whitelist=АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?;:()[]{}"\'-+= '
            
            # Извлекаем текст
            text = pytesseract.image_to_string(
                processed_image, 
                lang=self.lang, 
                config=config
            )
            
            return text.strip(), image
            
        except Exception as e:
            logger.error(f"Ошибка извлечения текста из {image_path}: {e}")
            return "", None
    
    def _preprocess_image(self, image: Image.Image) -> Image.Image:
        """Предобработка изображения для улучшения OCR"""
        # Конвертируем в массив numpy
        img_array = np.array(image)
        
        # Конвертируем в оттенки серого если цветное
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array
        
        # Увеличиваем контрастность
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced = clahe.apply(gray)
        
        # Устраняем шум
        denoised = cv2.medianBlur(enhanced, 3)
        
        # Бинаризация (черно-белое изображение)
        _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        return Image.fromarray(binary)
    
    def detect_text_regions(self, image: Image.Image) -> list:
        """Определение областей с текстом на изображении"""
        if not HAS_OCR:
            return []
            
        try:
            # Получаем данные о распознанном тексте с координатами
            img_array = np.array(image)
            data = pytesseract.image_to_data(img_array, lang=self.lang, output_type=pytesseract.Output.DICT)
            
            text_regions = []
            n_boxes = len(data['level'])
            
            for i in range(n_boxes):
                confidence = int(data['conf'][i])
                text = data['text'][i].strip()
                
                # Фильтруем только значимые области с текстом
                if confidence > 30 and text:
                    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                    text_regions.append({
                        'text': text,
                        'bbox': (x, y, x + w, y + h),
                        'confidence': confidence
                    })
            
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
    
    def _overlay_translation(self, image: Image.Image, translated_text: str, max_lines: int = 5) -> Image.Image:
        """Наложение перевода снизу изображения с ограничениями"""
        if not translated_text.strip():
            return image
        
        try:
            # Ограничиваем текст для отображения
            if len(translated_text) > 500:  # Максимум 500 символов для отображения
                translated_text = translated_text[:497] + "..."
            
            # Рассчитываем размеры для текста
            lines = self._wrap_text(translated_text, image.width - 40)
            
            # Ограничиваем количество строк
            if len(lines) > max_lines:
                lines = lines[:max_lines-1] + [lines[max_lines-1][:50] + "..."]
            
            line_height = 25
            text_height = len(lines) * line_height + 20
            
            # Ограничиваем максимальную высоту добавляемого текста
            max_text_height = min(text_height, 150)  # Максимум 150 пикселей для текста
            
            # Создаем новое изображение с дополнительным местом для текста
            new_height = image.height + max_text_height
            new_image = Image.new('RGB', (image.width, new_height), 'white')
            
            # Вставляем оригинальное изображение
            new_image.paste(image, (0, 0))
            
            # Рисуем полупрозрачный фон для текста
            overlay = Image.new('RGBA', (image.width, max_text_height), (255, 255, 255, 240))
            new_image.paste(overlay, (0, image.height), overlay)
            
            # Рисуем текст
            draw = ImageDraw.Draw(new_image)
            
            # Пытаемся загрузить системный шрифт
            try:
                if self.font_path:
                    font = ImageFont.truetype(self.font_path, 14)  # Чуть меньший размер
                else:
                    font = ImageFont.load_default()
            except:
                font = ImageFont.load_default()
            
            # Рисуем каждую строку
            y_offset = image.height + 10
            for line in lines:
                if y_offset + line_height > new_height - 5:  # Проверяем, помещается ли строка
                    break
                draw.text((20, y_offset), line, fill='black', font=font)
                y_offset += line_height
            
            return new_image
            
        except Exception as e:
            logger.error(f"Ошибка создания изображения с переводом: {e}")
            return imagetext: str) -> Image.Image:
        """Наложение перевода снизу изображения"""
        if not translated_text.strip():
            return image
        
        try:
            # Рассчитываем размеры для текста
            lines = self._wrap_text(translated_text, image.width - 40)
            line_height = 25
            text_height = len(lines) * line_height + 20
            
            # Создаем новое изображение с дополнительным местом для текста
            new_height = image.height + text_height
            new_image = Image.new('RGB', (image.width, new_height), 'white')
            
            # Вставляем оригинальное изображение
            new_image.paste(image, (0, 0))
            
            # Рисуем текст
            draw = ImageDraw.Draw(new_image)
            
            # Пытаемся загрузить системный шрифт
            try:
                if self.font_path:
                    font = ImageFont.truetype(self.font_path, 16)
                else:
                    font = ImageFont.load_default()
            except:
                font = ImageFont.load_default()
            
            # Рисуем каждую строку
            y_offset = image.height + 10
            for line in lines:
                draw.text((20, y_offset), line, fill='black', font=font)
                y_offset += line_height
            
            return new_image
            
        except Exception as e:
            logger.error(f"Ошибка создания изображения с переводом: {e}")
            return image
    
    def _replace_text_regions(self, image: Image.Image, original_text: str, translated_text: str) -> Image.Image:
        """Замена текстовых областей (сложная реализация)"""
        # Это более сложная функция, которая требует детекции и замены конкретных областей
        # Для упрощения пока возвращаем overlay
        logger.info("Замена текстовых областей пока не реализована, используется overlay")
        return self._overlay_translation(image, translated_text)
    
    def _wrap_text(self, text: str, max_width: int, char_width: int = 8) -> list:
        """Разбиение текста на строки по ширине"""
        words = text.split()
        lines = []
        current_line = ""
        max_chars = max_width // char_width
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            
            if len(test_line) <= max_chars:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                    current_line = word
                else:
                    # Если слово слишком длинное, разбиваем его
                    while len(word) > max_chars:
                        lines.append(word[:max_chars])
                        word = word[max_chars:]
                    current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines
    
    def process_image(self, src_path: str, dest_path: str, translate_func, 
                     glossary: dict = None, method: str = 'overlay') -> bool:
        """Полная обработка изображения с переводом"""
        try:
            # Создаем директории если нужно
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            # Извлекаем текст
            original_text, image = self.extract_text(src_path)
            
            if not original_text or not image:
                # Если текст не найден, копируем оригинал
                image_orig = Image.open(src_path)
                image_orig.save(dest_path)
                logger.info(f"Текст не найден, скопирован оригинал: {Path(src_path).name}")
                return True
            
            logger.debug(f"Извлеченный текст: {original_text[:100]}...")
            
            # Переводим текст
            translated_text = translate_func(original_text, glossary)
            
            logger.debug(f"Переведенный текст: {translated_text[:100]}...")
            
            # Создаем изображение с переводом
            result_image = self.create_translated_image(
                image, original_text, translated_text, method
            )
            
            # Сохраняем результат
            result_image.save(dest_path, quality=95, optimize=True)
            logger.info(f"✓ Обработано изображение: {Path(src_path).name}")
            
            return True
            
        except Exception as e:
            logger.error(f"Ошибка обработки изображения {src_path}: {e}")
            return False


def process_screenshot(src_path: str, dest_path: str, translate_func, 
                      glossary: dict = None, lang: str = 'rus') -> bool:
    """Удобная функция для обработки скриншотов"""
    processor = ImageTextProcessor(lang)
    return processor.process_image(src_path, dest_path, translate_func, glossary)


# Вспомогательные функции для совместимости с основным скриптом
def extract_text_from_image(image_path: str, lang: str = 'rus') -> tuple:
    """Обратная совместимость с основным скриптом"""
    processor = ImageTextProcessor(lang)
    return processor.extract_text(image_path)


def overlay_text_on_image(image: Image.Image, original_text: str, translated_text: str) -> Image.Image:
    """Обратная совместимость с основным скриптом"""
    processor = ImageTextProcessor()
    return processor._overlay_translation(image, translated_text)
