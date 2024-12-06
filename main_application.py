# main_application.py
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base
from login_window import LoginWindow
from project_management_window import ProjectManagementWindow
from code_collaboration_window import CodeCollaborationWindow

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Famous-Tech Collaboration")
        self.setGeometry(100, 100, 1200, 800)
        
        # Configuration de la base de données
        self.engine = create_engine('postgresql://neondb_owner:7H5fxkvBGbEI@ep-noisy-forest-a42ebqlz-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require')
        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)
        
        # Widget empilé pour la navigation
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Initialisation de la fenêtre de login
        self.login_window = LoginWindow(self.Session())
        self.login_window.login_success.connect(self.on_login_success)
        
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.setCurrentWidget(self.login_window)
    
    def on_login_success(self, user):
        # Fenêtre de gestion des projets
        self.project_window = ProjectManagementWindow(self.Session(), user)
        self.project_window.project_selected.connect(lambda project: self.open_code_collaboration(user, project))
        
        self.stacked_widget.addWidget(self.project_window)
        self.stacked_widget.setCurrentWidget(self.project_window)
    
    def open_code_collaboration(self, user, project):
        # Fenêtre de collaboration de code
        code_collab_window = CodeCollaborationWindow(self.Session(), user, project)
        self.stacked_widget.addWidget(code_collab_window)
        self.stacked_widget.setCurrentWidget(code_collab_window)