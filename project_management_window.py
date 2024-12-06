# project_management_window.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QLabel, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt, pyqtSignal
from sqlalchemy.exc import SQLAlchemyError
from models import Project

class ProjectManagementWindow(QWidget):
    project_selected = pyqtSignal(Project)
    
    def __init__(self, session, current_user):
        super().__init__()
        self.session = session
        self.current_user = current_user
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.projects_list = QListWidget()
        self.projects_list.itemDoubleClicked.connect(self.select_project)
        
        btn_layout = QHBoxLayout()
        
        create_project_btn = QPushButton("Créer Projet")
        create_project_btn.clicked.connect(self.create_project)
        
        refresh_btn = QPushButton("Actualiser")
        refresh_btn.clicked.connect(self.load_projects)
        
        btn_layout.addWidget(create_project_btn)
        btn_layout.addWidget(refresh_btn)
        
        layout.addWidget(QLabel("Vos Projets:"))
        layout.addWidget(self.projects_list)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        
        self.load_projects()
    
    def load_projects(self):
        self.projects_list.clear()
        try:
            projects = self.session.query(Project).filter_by(owner_id=self.current_user.id).all()
            for project in projects:
                item = QListWidgetItem(f"{project.name} - {project.status}")
                item.setData(Qt.UserRole, project)
                self.projects_list.addItem(item)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, "Erreur", f"Impossible de charger les projets: {str(e)}")
    
    def create_project(self):
        name, ok = QInputDialog.getText(self, "Nouveau Projet", "Nom du projet:")
        if ok and name:
            try:
                new_project = Project(
                    name=name, 
                    owner_id=self.current_user.id,
                    description=""
                )
                self.session.add(new_project)
                self.session.commit()
                self.load_projects()
            except SQLAlchemyError as e:
                QMessageBox.critical(self, "Erreur", f"Impossible de créer le projet: {str(e)}")
    
    def select_project(self, item):
        project = item.data(Qt.UserRole)
        self.project_selected.emit(project)