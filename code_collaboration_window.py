# code_collaboration_window.py
import warnings
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QComboBox, QPushButton, QLabel, QMessageBox
from sqlalchemy.exc import SQLAlchemyError
import black
from models import CodeSnippet

# Suppress the specific deprecation warning
warnings.filterwarnings("ignore", category=DeprecationWarning, module="PyQt5")

class CodeCollaborationWindow(QWidget):
    def __init__(self, session, current_user, project):
        super().__init__()
        self.session = session
        self.current_user = current_user
        self.project = project
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        project_info = QLabel(f"Projet: {self.project.name}")
        layout.addWidget(project_info)
        
        self.code_editor = QTextEdit()
        self.code_editor.setPlaceholderText("Écrivez ou collez votre code ici...")
        
        self.language_selector = QComboBox()
        self.language_selector.addItems([
            "Python", "JavaScript", "Java", "C++", "Ruby", 
            "PHP", "Swift", "Kotlin", "Go", "Rust"
        ])
        
        btn_layout = QHBoxLayout()
        
        save_btn = QPushButton("Sauvegarder")
        save_btn.clicked.connect(self.save_code_snippet)
        
        format_btn = QPushButton("Formater")
        format_btn.clicked.connect(self.format_code)
        
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(format_btn)
        
        layout.addWidget(QLabel("Langage:"))
        layout.addWidget(self.language_selector)
        layout.addWidget(self.code_editor)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
    
    def save_code_snippet(self):
        code = self.code_editor.toPlainText()
        language = self.language_selector.currentText()
        
        if code.strip():
            try:
                snippet = CodeSnippet(
                    project_id=self.project.id,
                    user_id=self.current_user.id,
                    code=code,
                    language=language
                )
                self.session.add(snippet)
                self.session.commit()
                QMessageBox.information(self, "Succès", "Code sauvegardé!")
            except SQLAlchemyError as e:
                QMessageBox.critical(self, "Erreur", f"Impossible de sauvegarder: {str(e)}")
    
    def format_code(self):
        try:
            code = self.code_editor.toPlainText()
            if self.language_selector.currentText() == "Python":
                formatted_code = black.format_str(code, mode=black.FileMode())
                self.code_editor.setPlainText(formatted_code)
            else:
                QMessageBox.warning(self, "Non supporté", "Formatage supporté uniquement pour Python")
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Formatage impossible: {str(e)}")