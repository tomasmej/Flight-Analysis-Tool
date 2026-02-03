import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog
from PySide6.QtCore import Qt
from ..backend.database.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription
from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel, QPalette, QColor
from orion.frontend.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Orion")
    app.setApplicationVersion("1.0")
    
    # palette = QPalette()
    # palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0))  
    # app.setPalette(palette)

    app.setStyle('Fusion')
    
    database_init()
    
    
    window = MainWindow()
    window.setWindowIcon(QIcon("assets/seds.png"))
    window.show()

    sys.exit(app.exec())

