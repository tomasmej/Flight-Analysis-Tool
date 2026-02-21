import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog, QInputDialog, QLineEdit, QFileDialog
from PySide6.QtCore import Qt
from ..ui.orion_v6 import Ui_mainWindow
from ..ui.ui_csv.browseCsv import Ui_csvDialog
# from ..backend.TrackerEngine import TrackerEngine
# from ..backend.ProfileEngine import ProfileEngine
from ..backend.database.database import *
from ..backend.database.database_csv import loadCsvNames
from orion.frontend.new_profile_dialog import NewProfileDialog
from pathlib import Path


class CsvWindow(QDialog):
    def __init__(self, trackerEngine, profileEngine, parent=None):
        super().__init__(parent)

        self.engine = trackerEngine
        self.engine.activate()

        self.engine_profile = profileEngine
        self.engine_profile.activate()
    
        print(loadCsvNames())

        self.ui = Ui_csvDialog()
        self.ui.setupUi(self)

        self.connections()
        self.refreshCsvList()
        self.refreshProfileList()

        self.setWindowTitle("CSVs")
        self.setBaseSize(600, 900)

     
    def connections(self):
    #         self.ui.profileList.itemClicked.connect(self.onItemClicked)
            self.ui.importButton.clicked.connect(self.importClicked)
            self.ui.deleteButton.clicked.connect(self.deleteClicked)

    def refreshCsvList(self):
        self.ui.csvList.clear()
        for i in self.engine.csvList:
            self.ui.csvList.addItem(str(i.name))

    def refreshProfileList(self):
        self.ui.profileBox.clear()
        for i in self.engine_profile.profileList:
            self.ui.profileBox.addItem(i)


    def importClicked(self): #import button clicked
        print('import clicked!')

        # open dialog
        selected_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import CSV",
            "",
            "CSV Files (*.csv)"
        )

        if not selected_path:
            return

        # create Path to csv file
        csv_path = Path(selected_path)

        # add absolute path to engine
        self.engine.addCsv(csv_path)
        self.engine.csvList.append(csv_path)
        print("Csv imported: " + csv_path.name)

        #add path name to ui 
        self.ui.csvList.addItem(csv_path.name)

    

    def deleteClicked(self):
        csvName = self.ui.csvList.currentItem().text()
        print("Csv to delete:", csvName)
        self.engine.deleteCsv(csvName)
        self.refreshCsvList()
