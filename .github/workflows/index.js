const fs = require('fs');
const path = require('path');
const axios = require('axios');

// --------------------------------------------------------
// Utils functions
// --------------------------------------------------------

/**
 * Writes a translated file to disk, creating directories if needed
 */
const writeTranslatedFile = ({ outputFilePath, text }) => {
  console.log('Writing:', outputFilePath);

  // Create directories if they don't exist (required for gitbook page-groups)
  const outputDir = outputFilePath.substring(0, outputFilePath.lastIndexOf('/'));
  fs.mkdirSync(outputDir, { recursive: true });

  // Write the translated file to disk
  fs.writeFileSync(outputFilePath, text);
};

/**
 * Finds a file by searching upward through parent directories.
 * @param {string} fileName - The name of the file to search for.
 * @param {string} [startDir=process.cwd()] - The directory to start searching from.
 * @returns {string|null} - The absolute path of the found file or null if not found.
 */
const findFileUpward = (fileName, startDir = process.cwd()) => {
  console.log('Trying to locate file', fileName);
  
  let currentDir = startDir;

  while (true) {
    const filePath = path.join(currentDir, fileName);
    if (fs.existsSync(filePath)) {
      return filePath; // found the file
    }

    const parentDir = path.dirname(currentDir);
    if (parentDir === currentDir) {
      // reached the root directory
      return null;
    }

    currentDir = parentDir; // move up to the parent directory
  }
};

// --------------------------------------------------------
// Azure Translator class
// --------------------------------------------------------

class AzureTranslator {
  #credentials;
  #url;

  constructor({ apiKey, region, url }) {
    if (!apiKey || !region || !url) {
      throw new Error('Must specify a translator service apiKey, region and url');
    }

    this.#credentials = {
      'Ocp-Apim-Subscription-Key': apiKey,
      'Ocp-Apim-Subscription-Region': region,
    };
    this.#url = url;
  }

  /**
   * Translate a document into a target language
   */
  async translateFile({ filePath, sourceLanguage, targetLanguage }) {
    // Read file and convert to Blob
    const fileBuffer = await fs.promises.readFile(filePath);
    const blob = new Blob([fileBuffer], { type: 'text/markdown' });
    const form = new FormData();
    form.append('document', blob);

    // Make translation request to Azure
    const response = await axios.post(
      `${this.#url}/translator/document:translate`,
      form,
      {
        headers: {
          ...this.#credentials,
          'Content-Type': 'multipart/form-data'
        },
        params: {
          'api-version': '2024-05-01',
          sourceLanguage,
          targetLanguage,
        },
        responseType: 'arraybuffer'
      }
    );

    // AzureTranslator's translations are not perfect, so we need
    // to fix some issues manually, using regex.
    const outputText = response.data.toString()
      // Fix file metadata
      .replaceAll(`description : `, `description: `)
      .replaceAll(`couvertureY : `, `coverY: `)
      .replaceAll(`Couverture : `, `cover: `)
      // Fix hints
      .replaceAll('{% hint style="avertissement » %}', '{% hint style="warning" %}')
      .replaceAll('{% hint style="info » %}', '{% hint style="info" %}')
      .replaceAll('{% hint style="danger » %}', '{% hint style="danger" %}')
      // Fix bold syntax
      .replaceAll(/(\S)\*\*/g, '$1 **')               // Ensure space before **
      .replaceAll(/\*\*(\S)/g, '** $1')               // Ensure space after **
      .replaceAll(/\*\*\s+([^*]+)\s+\*\*/g, '**$1**') // Remove spaces between asterisks
      // Fix weird separators
      .replaceAll('* **', '***');
      
    return outputText;
  }
}

// --------------------------------------------------------
// Main script execution
// --------------------------------------------------------

async function main() {
  // -----------------------------------------------------------
  // 1. Initialize the script: read config and setup translator
  // -----------------------------------------------------------

  const SOURCE_LANGUAGE = process.env.SOURCE_LANGUAGE;
  const TARGET_LANGUAGE = process.env.TARGET_LANGUAGE;
  const translatorApiKey = process.env.TRANSLATOR_API_KEY;

  if (!SOURCE_LANGUAGE) {
    throw new Error('SOURCE_LANGUAGE is not set');
  }

  if (!TARGET_LANGUAGE) {
    throw new Error('TARGET_LANGUAGE is not set');
  }

  if (!translatorApiKey) {
    throw new Error('TRANSLATOR_API_KEY is not set');
  }

  if (!process.env.NEW_FILES) {
    throw new Error('NEW_FILES is not set');
  }

  const AzTranslator = new AzureTranslator({
    apiKey: translatorApiKey,
    region: 'francecentral',
    url: 'https://365t-translator-dev.cognitiveservices.azure.com'
  });

  // --------------------------------------------------------
  // 2. Translate files
  // --------------------------------------------------------

  const filesToTranslate = process.env.NEW_FILES.split(' ');

  // Force updating SUMMARY.md to make sure Gitbook pages paths are correct
  filesToTranslate.push(`${SOURCE_LANGUAGE}/SUMMARY.md`);

  for (const file of filesToTranslate) {
    const fileName = file.trim();
    const inputFilePath = findFileUpward(fileName);
    
    if (!inputFilePath) {
      console.error('File not found:', fileName);
      continue;
    }

    const translatedText = await AzTranslator.translateFile({
      filePath: inputFilePath,
      sourceLanguage: SOURCE_LANGUAGE,
      targetLanguage: TARGET_LANGUAGE
    });

    const outputFilePath = inputFilePath.replace(fileName, `${TARGET_LANGUAGE}/${fileName.split(`${SOURCE_LANGUAGE}/`)[1]}`);
    
    writeTranslatedFile({
      outputFilePath,
      text: translatedText,
    });
  }
}

// Execute the main function
main().catch(error => {
  console.error('Error:', error);
  process.exit(1);
});
