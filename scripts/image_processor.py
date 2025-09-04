#!/usr/bin/env python3
"""
Модуль для обработки и перевода текста на скриншотах.
"""

import os
import cv2
import numpy as np
from PIL import Image
import pytesseract
import re

def extract_text_from_image(image_path, lang='rus'):
    """Извлечение текста с изображения с помощью Tesseract OCR"""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)
    return text, image

def overlay_text_on_image(image, original_text, translated_text):
    """
    Замена текста на изображении.
    Упрощенная реализация - на практике可能需要 более сложная обработка.
    """
    # Конвертируем PIL Image в OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Здесь должна быть сложная логика detection и replacement текста
    # Для демонстрации просто добавим перевод внизу изображения
    
    # Увеличиваем canvas для добавления текста
    height, width = image_cv.shape[:2]
    new_height = height + 100
    new_image = np.ones((new_height, width, 3), dtype=np.uint8) * 255
    new_image[:height, :] = image_cv
    
    # Добавляем перевод
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(translated_text, font, 0.7, 2)[0]
    text_x = (width - text_size[0]) // 2
    text_y = height + 70
    
    cv2.putText(
        new_image, 
        translated_text, 
        (text_x, text_y), 
        font, 
        0.7, 
        (0, 0, 0), 
        2, 
        cv2.LINE_AA
    )
    
    return Image.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))

def process_image(src_path, dest_path, model, tokenizer, glossary):
    """Обработка и перевод скриншота"""
    print(f"Processing image: {src_path}")
    
    # Извлекаем текст с изображения
    original_text, image = extract_text_from_image(src_path)
    
    if not original_text.strip():
        # Если текст не найден, просто копируем изображение
        image.save(dest_path)
        return
    
    # Переводим извлеченный текст
    translated_text = translate_text(original_text, model, tokenizer, glossary)
    
    # Создаем новое изображение с переведенным текстом
    new_image = overlay_text_on_image(image, original_text, translated_text)
    new_image.save(dest_path)

def translate_text(text, model, tokenizer, glossary=None):
    """Перевод текста (упрощенная версия)"""
    if glossary:
        for term, translation in glossary.items():
            text = re.sub(r'\b' + re.escape(term) + r'\b', translation, text, flags=re.IGNORECASE)
    
    # В реальной реализации здесь будет вызов модели перевода
    # Для демонстрации возвращаем заглушку
    return f"Translated: {text}"
