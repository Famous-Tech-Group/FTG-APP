# main.py
import sys
from PyQt5.QtWidgets import QApplication
from main_application import MainApplication

def main():
    app = QApplication(sys.argv)
    main_app = MainApplication()
    main_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()