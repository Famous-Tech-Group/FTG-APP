# elegant_chat.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer
from datetime import datetime

class ElegantChatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        message_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Message éphémère...")
        
        send_btn = QPushButton("🚀")
        send_btn.clicked.connect(self.send_message)
        
        message_layout.addWidget(self.message_input)
        message_layout.addWidget(send_btn)
        
        layout.addWidget(self.chat_area)
        layout.addLayout(message_layout)
        
        self.setLayout(layout)
    
    def send_message(self):
        message = self.message_input.text().strip()
        if message:
            timestamp = datetime.now().strftime("%H:%M")
            formatted_message = f"<b>[{timestamp}]</b> {message}"
            
            self.chat_area.append(formatted_message)
            self.message_input.clear