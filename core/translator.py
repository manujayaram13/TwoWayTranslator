from googletrans import Translator

translator = Translator()

def detect_language(text):
    detection = translator.detect(text)
    return detection.lang

def translate_text(text, src='auto', dest='en'):
    translated = translator.translate(text, src=src, dest=dest)
    return translated.text
