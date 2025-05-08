from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit,
    QPushButton, QComboBox, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from core.translator import translate_text
from core.tts import speak
import sys

languages = {
    'English': 'en', 
    'Hindi': 'hi', 
    'French': 'fr', 
    'Spanish': 'es', 
    'German': 'de', 
    'Kannada': 'kn', 
    'Telugu': 'te', 
    'Japanese': 'ja', 
    'Chinese': 'zh-cn', 
    'Arabic': 'ar', 
    'Bengali': 'bn', 
    'Portuguese': 'pt', 
    'Russian': 'ru', 
    'Italian': 'it', 
    'Dutch': 'nl', 
    'Korean': 'ko', 
    'Turkish': 'tr', 
    'Tamil': 'ta', 
    'Urdu': 'ur', 
    'Punjabi': 'pa', 
    'Marathi': 'mr', 
    'Gujarati': 'gu', 
    'Thai': 'th', 
    'Vietnamese': 'vi', 
    'Swahili': 'sw', 
    'Malay': 'ms', 
    'Filipino': 'tl', 
    'Greek': 'el', 
    'Hebrew': 'he', 
    'Polish': 'pl', 
    'Hungarian': 'hu', 
    'Czech': 'cs', 
    'Romanian': 'ro', 
    'Bulgarian': 'bg', 
    'Serbian': 'sr', 
    'Swedish': 'sv', 
    'Danish': 'da', 
    'Finnish': 'fi', 
    'Norwegian': 'no'
}

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✨ Two-Way Translator ✨")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        # Layout
        layout = QVBoxLayout()

        # Input Text
        self.input_label = QLabel("📝 Enter text:")
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Type here...")
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)

        # Language Selection
        lang_layout = QHBoxLayout()
        self.from_lang = QComboBox()
        self.from_lang.addItems(languages.keys())
        self.to_lang = QComboBox()
        self.to_lang.addItems(languages.keys())
        lang_layout.addWidget(QLabel("🌍 From:"))
        lang_layout.addWidget(self.from_lang)
        lang_layout.addWidget(QLabel("➡️ To:"))
        lang_layout.addWidget(self.to_lang)
        layout.addLayout(lang_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.translate_button = QPushButton("💬 Translate")
        self.translate_button.clicked.connect(self.translate)
        self.swap_button = QPushButton("🔄 Swap")
        self.swap_button.clicked.connect(self.swap_languages)
        self.speak_button = QPushButton("🎤 Speak")
        self.speak_button.clicked.connect(self.speak_output)
        self.clear_button = QPushButton("❌ Clear")
        self.clear_button.clicked.connect(self.clear_all)
        button_layout.addWidget(self.translate_button)
        button_layout.addWidget(self.swap_button)
        button_layout.addWidget(self.speak_button)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)

        # Output Text
        self.output_label = QLabel("🌟 Translated text:")
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("background-color: ;")
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)

        # Set the layout
        self.setLayout(layout)

        # Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #282c34;
                color: white;
            }
            QLabel {
                font-size: 18px;
                color: #f0f0f0;
            }
            QTextEdit {
                font-size: 16px;
                border: 2px solid #4caf50;
                padding: 5px;
                border-radius: 8px;
                background-color: #1c1f27;
                color: #d1d1d1;
            }
            QPushButton {
                background-color: #4caf50;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388e3c;
            }
        """)

    def translate(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "⚠️ Warning", "Input text is empty!")
            return

        src_lang = languages[self.from_lang.currentText()]
        tgt_lang = languages[self.to_lang.currentText()]

        try:
            translated = translate_text(text, src=src_lang, dest=tgt_lang)
            self.output_text.setText(translated)
        except Exception as e:
            QMessageBox.critical(self, "❌ Error", str(e))

    def swap_languages(self):
        from_idx = self.from_lang.currentIndex()
        to_idx = self.to_lang.currentIndex()
        self.from_lang.setCurrentIndex(to_idx)
        self.to_lang.setCurrentIndex(from_idx)

    def speak_output(self):
        text = self.output_text.toPlainText()
        lang = languages[self.to_lang.currentText()]
        if text:
            speak(text, lang)

    def clear_all(self):
        self.input_text.clear()
        self.output_text.clear()

def run_gui():
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())
