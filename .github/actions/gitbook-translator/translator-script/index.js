const axios = require('axios');
const { v4: uuidv4 } = require('uuid');
const fs = require('fs');
const path = require('path');

const AZURE_TRANSLATOR_ENDPOINT = 'https://api.cognitive.microsofttranslator.com';
const API_KEY = process.env.TRANSLATOR_API_KEY;
const SOURCE_LANGUAGE = process.env.SOURCE_LANGUAGE;
const TARGET_LANGUAGE = process.env.TARGET_LANGUAGE;
const NEW_FILES = process.env.NEW_FILES?.split(' ') || [];

// Функция для перевода текста
async function translateText(text, from, to) {
  try {
    const response = await axios({
      baseURL: AZURE_TRANSLATOR_ENDPOINT,
      url: '/translate',
      method: 'post',
      headers: {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Content-type': 'application/json',
        'X-ClientTraceId': uuidv4().toString()
      },
      params: {
        'api-version': '3.0',
        'from': from,
        'to': to
      },
      data: [{
        'text': text
      }]
    });

    return response.data[0].translations[0].text;
  } catch (error) {
    console.error('Translation error:', error.response?.data || error.message);
    throw error;
  }
}

// Функция для сохранения переведенного контента
function saveTranslatedContent(filePath, content) {
  const targetPath = filePath.replace(SOURCE_LANGUAGE, TARGET_LANGUAGE);
  const targetDir = path.dirname(targetPath);
  
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  
  fs.writeFileSync(targetPath, content, 'utf8');
  console.log(`Translated and saved: ${targetPath}`);
}

// Функция для обработки markdown файлов
function processMarkdownElements(content) {
  // Сохраняем специальные markdown элементы
  const preservePatterns = [
    /```[\s\S]*?```/g,          // Блоки кода
    /`[^`]+`/g,                 // Inline код
    /!\[.*?\]\(.*?\)/g,         // Изображения
    /\[.*?\]\(.*?\)/g,          // Ссылки
    /#{1,6}\s/g,                // Заголовки
    /^\s*[-*+]\s/gm,            // Списки
    /^\s*\d+\.\s/gm,            // Нумерованные списки
    /\*\*.*?\*\*/g,             // Жирный текст
    /\*.*?\*/g,                 // Курсив
    /~~.*?~~/g,                 // Зачеркнутый текст
  ];
  
  return content;
}

// Основная функция
async function main() {
  if (!API_KEY) {
    console.error('TRANSLATOR_API_KEY environment variable is required');
    process.exit(1);
  }

  console.log(`Translating from ${SOURCE_LANGUAGE} to ${TARGET_LANGUAGE}`);
  console.log(`Files to translate: ${NEW_FILES.join(', ')}`);

  for (const filePath of NEW_FILES) {
    if (!filePath.endsWith('.md')) {
      console.log(`Skipping non-markdown file: ${filePath}`);
      continue;
    }

    try {
      console.log(`Processing: ${filePath}`);
      
      const content = fs.readFileSync(filePath, 'utf8');
      
      // Разбиваем контент на параграфы для лучшего перевода
      const paragraphs = content.split('\n\n');
      const translatedParagraphs = [];
      
      for (const paragraph of paragraphs) {
        if (paragraph.trim()) {
          // Пропускаем блоки кода и другие специальные элементы
          if (paragraph.startsWith('```') || paragraph.match(/^!\[.*?\]\(.*?\)/)) {
            translatedParagraphs.push(paragraph);
          } else {
            const translatedParagraph = await translateText(paragraph, SOURCE_LANGUAGE, TARGET_LANGUAGE);
            translatedParagraphs.push(translatedParagraph);
          }
        } else {
          translatedParagraphs.push(paragraph);
        }
      }
      
      const translatedContent = translatedParagraphs.join('\n\n');
      saveTranslatedContent(filePath, translatedContent);
      
    } catch (error) {
      console.error(`Error processing ${filePath}:`, error.message);
    }
  }
}

main().catch(console.error);
