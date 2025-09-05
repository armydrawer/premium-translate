# Автоматический переводчик документации

Система для автоматического перевода технической документации с русского языка на английский с использованием AI моделей и OCR для изображений.

## Основные возможности

- 🤖 **AI-перевод** с использованием моделей Helsinki-NLP
- 📄 **Обработка Markdown** с сохранением форматирования
- 🖼️ **OCR для изображений** с извлечением и переводом текста
- 📊 **Ограничения ресурсов** для стабильной работы
- 🔧 **Гибкая настройка** через конфигурационные файлы
- 📈 **Мониторинг производительности**

## Ограничения по умолчанию

### Размеры файлов и текста
- **Максимальный размер файла**: 1 MB
- **Максимальный размер изображения**: 10 MB
- **Максимум символов за один перевод**: 10,000
- **Максимум токенов на вход модели**: 512
- **Максимум текста на изображении**: 5,000 символов

### Системные ресурсы
- **Лимит памяти**: 2 GB
- **Таймаут на файл**: 300 секунд
- **Максимум строк перевода на изображении**: 5

## Установка

### 1. Установка зависимостей

```bash
# Системные зависимости (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-rus tesseract-ocr-eng

# Python зависимости
pip install -r requirements.txt
```

### 2. Структура проекта

```
project/
├── scripts/
│   ├── translate.py           # Основной скрипт
│   ├── image_processor.py     # Обработка изображений
│   ├── requirements.txt       # Зависимости
│   ├── glossary.json         # Глоссарий терминов
│   └── translation_config.json # Конфигурация
├── ru/                       # Исходные файлы (русский)
├── en/                       # Переведенные файлы (английский)
└── .github/workflows/
    └── translate.yml         # GitHub Actions
```

## Использование

### Базовое использование

```bash
# Простой перевод с AI
python scripts/translate.py --source_dir ./ru --target_dir ./en

# Перевод без AI (только глоссарий)
python scripts/translate.py --no-ai --glossary scripts/glossary.json

# Принудительный перевод всех файлов
python scripts/translate.py --force --verbose
```

### Расширенные параметры

```bash
python scripts/translate.py \
    --source_dir ./ru \
    --target_dir ./en \
    --glossary scripts/glossary.json \
    --config scripts/translation_config.json \
    --max-chars 8000 \
    --max-tokens 400 \
    --max-file-size 2097152 \
    --check-resources \
    --verbose
```

### Параметры командной строки

| Параметр | Описание | По умолчанию |
|----------|----------|-------------|
| `--source_dir` | Папка с исходными файлами | `./ru` |
| `--target_dir` | Папка для переведенных файлов | `./en` |
| `--glossary` | Путь к файлу глоссария | - |
| `--config` | Путь к файлу конфигурации | - |
| `--force` | Принудительный перевод всех файлов | `false` |
| `--no-ai` | Отключить AI перевод | `false` |
| `--verbose` | Подробный вывод | `false` |
| `--max-chars` | Макс. символов на кусок | `10000` |
| `--max-tokens` | Макс. токенов на вход | `512` |
| `--max-file-size` | Макс. размер файла (байты) | `1048576` |
| `--check-resources` | Проверить ресурсы системы | `false` |

## Конфигурация

### Пример glossary.json

```json
{
  "API": "API",
  "Docker": "Docker",
  "Kubernetes": "Kubernetes",
  "микросервис": "microservice",
  "контейнер": "container",
  "развертывание": "deployment",
  "мониторинг": "monitoring",
  "логирование": "logging",
  "балансировщик нагрузки": "load balancer",
  "база данных": "database",
  "аутентификация": "authentication",
  "авторизация": "authorization"
}
```

### Пример translation_config.json

```json
{
  "limits": {
    "max_chars_per_chunk": 10000,
    "max_tokens_per_input": 512,
    "max_file_size_bytes": 1048576,
    "max_image_size_bytes": 10485760
  },
  "translation": {
    "model_name": "Helsinki-NLP/opus-mt-ru-en",
    "beam_size": 3,
    "temperature": 0.8
  },
  "performance": {
    "memory_limit_mb": 2048,
    "timeout_per_file_seconds": 300
  }
}
```

## GitHub Actions

Автоматический перевод при изменениях в папке `ru/`:

```yaml
# Ручной запуск с параметрами
gh workflow dispatch translate.yml \
  -f force_retranslate=true \
  -f translation_method=ai

# Или через веб-интерфейс GitHub
```

### Параметры workflow

- **force_retranslate**: Принудительный перевод всех файлов
- **translation_method**: Метод перевода (`ai` или `simple`)

## Мониторинг и отладка

### Проверка ресурсов

```bash
# Проверка перед запуском
python scripts/translate.py --check-resources --verbose

# Мониторинг во время работы
python scripts/translate.py --verbose 2>&1 | tee translation.log
```

### Типичные ошибки и решения

| Ошибка | Причина | Решение |
|--------|---------|---------|
| `OutOfMemoryError` | Недостаточно памяти | Уменьшить `max_chars_per_chunk` |
| `Model not found` | Нет доступа к HuggingFace | Установить `HF_TOKEN` |
| `Tesseract not found` | OCR не установлен | Установить `tesseract-ocr` |
| `File too large` | Превышен лимит размера | Увеличить `max_file_size` |

### Логи и диагностика

```bash
# Подробные логи
python scripts/translate.py --verbose --source_dir ./ru --target_dir ./en

# Проверка конкретного файла
python scripts/translate.py --verbose --source_dir ./ru/specific_file.md --force

# Только проверка без перевода
python scripts/translate.py --no-ai --verbose
```

## Производительность

### Рекомендуемые настройки

**Для быстрой работы:**
```bash
--max-chars 5000 --max-tokens 256 --no-ai
```

**Для качественного перевода:**
```bash
--max-chars 15000 --max-tokens 512 --check-resources
```

**Для больших проектов:**
```bash
--max-file-size 2097152 --config scripts/translation_config.json
```

### Оптимизация

1. **Используйте GPU** для ускорения AI перевода
2. **Настройте лимиты** под ваши ресурсы
3. **Используйте глоссарий** для специальных терминов
4. **Мониторьте память** при обработке больших файлов

## Поддерживаемые форматы

- **Текст**: `.md`, `.txt`, `.rst`
- **Изображения**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`
- **Копирование**: все остальные файлы копируются без изменений

## Контроль качества

Система автоматически:
- ✅ Сохраняет структуру Markdown
- ✅ Не переводит блоки кода
- ✅ Сохраняет ссылки и изображения
- ✅ Применяет глоссарий терминов
- ✅ Проверяет размеры файлов
- ✅ Мониторит использование ресурсов

## Лицензия

MIT License - см. файл LICENSE для деталей.
