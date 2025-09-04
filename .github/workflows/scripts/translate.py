import os
import subprocess
import requests
import re
from bs4 import BeautifulSoup
import markdown

# --- КОНФИГУРАЦИЯ ---
SOURCE_DIR = "ru"
TARGET_DIR = "en"
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate" # Используйте https://api.deepl.com для Pro

# --- 1. ОПРЕДЕЛЕНИЕ ИЗМЕНЕННЫХ ФАЙЛОВ ---

def get_changed_files():
    """Возвращает список измененных файлов в последнем коммите в папке SOURCE_DIR."""
    # Получаем хэш предпоследнего коммита
    result = subprocess.run(['git', 'rev-parse', 'HEAD~1'], capture_output=True, text=True)
    if result.returncode != 0:
        # Если это первый коммит, сравниваем с пустым деревом
        parent_commit = '4b825dc642cb6eb9a060e54bf8d69288fbee4904' # Пустое дерево Git
    else:
        parent_commit = result.stdout.strip()
        
    # Получаем список измененных файлов между двумя коммитами
    result = subprocess.run(
        ['git', 'diff', '--name-only', parent_commit, 'HEAD', '--', SOURCE_DIR],
        capture_output=True,
        text=True
    )
    changed_files = result.stdout.strip().split('\n')
    return [f for f in changed_files if f]

# --- 2. ЛОГИКА ПЕРЕВОДА ---

def translate_text_deepl(text, target_lang="EN-US"):
    """Переводит текст с помощью DeepL API, сохраняя теги HTML."""
    if not text.strip():
        return ""
        
    headers = {"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"}
    params = {
        "text": text,
        "target_lang": target_lang,
        "source_lang": "RU",
        "tag_handling": "html", # Важно для сохранения разметки
    }
    
    response = requests.post(DEEPL_API_URL, headers=headers, data=params)
    response.raise_for_status()
    return response.json()["translations"][0]["text"]

def translate_markdown_file(source_path, target_path):
    """Читает MD, конвертирует в HTML, переводит и сохраняет обратно в MD."""
    print(f"Translating Markdown file: {source_path} -> {target_path}")
    
    with open(source_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Конвертируем Markdown в HTML для корректной обработки тегов API
    html_content = markdown.markdown(md_content)
    
    # Разделяем на большие куски, чтобы не превышать лимиты API и сохранить структуру
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for element in soup.find_all(string=True):
        # Пропускаем текст внутри тегов code, pre и т.д.
        if element.parent.name in ['pre', 'code']:
            continue
        
        original_text = str(element)
        if original_text.strip(): # Переводим только непустые строки
            translated_text = translate_text_deepl(original_text)
            element.replace_with(translated_text)

    # В GitBook заголовки часто являются ссылками, их нужно обработать
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if header.string and header.string.strip():
             # Логика для перевода заголовков (может потребовать доработки под вашу структуру)
             pass

    # Перевод должен быть выполнен обратно в Markdown, что является сложной задачей.
    # Простой подход: переводить текст по абзацам.
    
    translated_lines = []
    # Простая реализация: переводим абзацы, игнорируя сложную разметку
    for line in md_content.split('\n'):
        # Игнорируем блоки кода
        if line.strip().startswith("```"):
            translated_lines.append(line)
            continue
            
        # Простая проверка на заголовок или текст
        if re.match(r'^(#+\s|\s*[-*+]\s|[0-9]+\.\s)', line) or (line.strip() and not line.startswith("![")):
             translated_lines.append(translate_text_deepl(line))
        else:
            translated_lines.append(line)
    
    translated_content = "\n".join(translated_lines)
    
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    print("Translation successful.")


def handle_image_change(source_path, target_path):
    """Копирует изображение и создает Issue для ручного перевода (Подход А)."""
    print(f"Image changed: {source_path}. Copying and creating an issue.")
    
    # 1. Копируем изображение в /en, чтобы ссылка не была битой
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    import shutil
    shutil.copy2(source_path, target_path)
    
    # 2. Создаем Issue на GitHub (требует GITHUB_TOKEN)
    issue_title = f"Manual Translation Required for Image: {target_path}"
    issue_body = f"The following image has been updated in Russian and needs to be manually translated to English:\n\n`{source_path}`\n\nPlease update the target file:\n`{target_path}`"
    
    repo = os.getenv("GITHUB_REPOSITORY")
    token = os.getenv("GITHUB_TOKEN")
    
    if not (repo and token):
        print("GITHUB_REPOSITORY or GITHUB_TOKEN not found. Skipping issue creation.")
        return

    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": issue_title, "body": issue_body, "labels": ["translation", "images"]}
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Successfully created issue for {source_path}")
    else:
        print(f"Failed to create issue: {response.content}")

# --- 3. ОСНОВНОЙ ЦИКЛ ---

def main():
    if not DEEPL_API_KEY:
        print("Error: DEEPL_API_KEY secret not found.")
        return

    changed_files = get_changed_files()
    if not changed_files:
        print("No changes found in the 'ru' directory. Exiting.")
        return

    print(f"Detected changes in: {changed_files}")

    for rel_path in changed_files:
        source_path = rel_path
        target_path = rel_path.replace(SOURCE_DIR, TARGET_DIR, 1)

        if source_path.endswith(".md"):
            translate_markdown_file(source_path, target_path)
        elif source_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Для изображений используем Подход А
            handle_image_change(source_path, target_path)

if __name__ == "__main__":
    main()
