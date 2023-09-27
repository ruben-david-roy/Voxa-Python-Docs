# Voxa
*The Voxa Language Translation Service*

Voxa is an easy-to-use Python package designed to translate text. 

## Table of Contents
- [Getting Started 🚀](#getting-started-🚀)
- [Usage 📖](#usage-📖)
- [Multi-tasking 🔥](#multi-tasking-🔥)

## Getting Started 🚀
To get started, install Voxa with pip:
```bash
pip install voxa
```

## Usage 📖
Using Voxa is straightforward. Below is a quick example to translate an English text into French:
```python
import voxa

translator = voxa.Translator(source='en', target='fr')

translated_text = translator.translate("Hello")

print(translated_text)
```

# Multi-tasking 🔥
```python
import voxa

# Create a Translator object with default languages
translator = voxa.Translator(source='en', target='fr')

# Translate "Hello" from English to French
translated_text = translator.translate("Hello")

# For one-off translations with different languages
spanish_translation = translator.translate("Hello", target='es')

print("Translation (English to French):", translated_text)
print("Translation (English to Spanish):", spanish_translation)
```