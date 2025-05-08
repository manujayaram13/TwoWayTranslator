from gtts import gTTS
import os
import tempfile

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        path = f.name
    tts.save(path)
    os.system(f'start {path}' if os.name == 'nt' else f'mpg123 {path}')
