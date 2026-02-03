import sys
import csv
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from ..backend.database.database import database_init
from PySide6.QtGui import QIcon
from orion.frontend.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Orion")
    app.setApplicationVersion("1.0")
    
    

    app.setStyle('Fusion')
    
    database_init()
    
    
    window = MainWindow()

    window.show()

    sys.exit(app.exec())

