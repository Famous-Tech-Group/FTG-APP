# login_window.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
import hashlib
from sqlalchemy.exc import SQLAlchemyError
from models import User

class LoginWindow(QWidget):
    login_success = pyqtSignal(User)
    
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        logo_label = QLabel()
        pixmap = QPixmap('logo.png')
        logo_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignCenter)
        
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow("Nom d'utilisateur:", self.username_input)
        form_layout.addRow("Mot de passe:", self.password_input)
        
        login_btn = QPushButton("Connexion")
        login_btn.clicked.connect(self.authenticate)
        
        layout.addWidget(logo_label)
        layout.addLayout(form_layout)
        layout.addWidget(login_btn)
        
        self.setLayout(layout)
    
    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        try:
            user = self.session.query(User).filter_by(
                username=username, 
                password_hash=hashed_password
            ).first()
            
            if user:
                self.login_success.emit(user)
            else:
                QMessageBox.warning(self, "Erreur", "Identifiants incorrects")
        
        except SQLAlchemyError as e:
            QMessageBox.critical(self, "Erreur de Base de Données", 
                                 f"Impossible de se connecter: {str(e)}")
        finally:
            self.session.close()