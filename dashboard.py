# dashboard.py
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from code_collaboration_window import CodeCollaborationWindow
from elegant_chat import ElegantChatWidget

class FamousTechDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Famous-Tech Communication Platform")
        self.setGeometry(100, 100, 1600, 900)
        
        self.main_tab_widget = QTabWidget()
        
        self.code_collaboration = CodeCollaborationWindow()
        self.elegant_chat = ElegantChatWidget()
        
        self.main_tab_widget.addTab(self.code_collaboration, "🖥️ Code Collaboration")
        self.main_tab_widget.addTab(self.elegant_chat, "💬 Chat Éphémère")
        
        self.setCentralWidget(self.main_tab_widget)