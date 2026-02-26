import sys
import csv
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from ..ui.orion_v7 import Ui_mainWindow
from ..ui.ui_profile.profile2 import Ui_Dialog
from ..ui.ui_csv.browseCsv import Ui_csvDialog
from ..backend.TrackerEngine import TrackerEngine
from ..backend.ProfileEngine import ProfileEngine
from ..backend.database.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription
from ..backend.database.database_csv import verifyDatabaseToDisk
from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel, QPalette, QColor
from orion.frontend.profile_window import ProfileWindow
from orion.frontend.csv_window import CsvWindow
from ..backend.utils.paths import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


        self.connections()

        # Tracker engine handles CSV logic
        self.trackerEngine = TrackerEngine()
        self.refreshCsvList()

        # Profile engine handles profile logic, creates Default profile if it does not exist
        self.profileEngine = ProfileEngine()
        self.profileEngine.createDefault()
        self.profileEngine.grabProfiles()
        self.refreshProfileList()

        data_folder = data_path()
        # print(data_folder)

        # if database gets recreated with populated data folder already existing, all csvs assigned to master profile
        if data_folder.exists():
            if verifyDatabaseToDisk(data_path(), self.trackerEngine.csvList):
                message = QMessageBox()
                message.information(QWidget(), "Info", "Database directory modified or deleted. Csvs have been refactored. ")
        else:
            print("No data folder to validate.")

        self.setXAttributes(self.ui.profileList.currentText())
        self.setYAttributes(self.ui.profileList.currentText())


        self.ui.stackedWidget.setCurrentIndex(0)

        self.setWindowTitle("Orion")
        self.setBaseSize(800, 600)

    def connections(self):
        self.ui.importButton.clicked.connect(self.import_clicked)
        self.ui.graphButton.clicked.connect(self.graph_clicked)
        self.ui.sheetButton.clicked.connect(self.sheet_clicked)
        self.ui.resetButton.clicked.connect(self.dual_clicked)
        self.ui.profileButton.clicked.connect(self.openCsvWindow)
        self.ui.configButton.clicked.connect(self.openProfileWindow)

        self.ui.profileList.currentTextChanged.connect(self.onProfileSelected)
        
        print('connected')

    def import_clicked(self): #import button clicked
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

        # add absolute path to engine, path name to database
        self.trackerEngine.addCsv(csv_path)
        self.trackerEngine.csvList.append(csv_path)
        print("Csv imported: " + csv_path.name)

        #add path name to ui 
        self.ui.csvList.addItem(csv_path.name)



    def graph_clicked(self): #graph button clicked
        print('Switching to graph view')       

        if self.display_graph(self.ui.csvList.currentText(), self.ui.xAttributeBox.currentText(), self.ui.yAttributeBox.currentText()) == -1:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.stackedWidget.setCurrentIndex(1)
    


    def sheet_clicked(self): #sheet button clicked
        print('Switching to sheet view')

        if self.display_sheet(self.ui.csvList.currentText()) == -1:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.stackedWidget.setCurrentIndex(2)

    def dual_clicked(self): #dual view button clicked
        print('Switching to dual view')

        if self.display_dual(self.ui.csvList.currentText(), self.ui.xAttributeBox.currentText(), self.ui.yAttributeBox.currentText()) == -1:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.stackedWidget.setCurrentIndex(3)


    def display_graph(self, csvname, xAttribute, yAttribute): #display graph with currently selected path and selected attributes
        path = self.trackerEngine.getStoredPath(csvname)
    
        if path is None:
            print("No CSV selected.")
            return -1
            
        xAxis, yAxis = self.trackerEngine.extract(path, xAttribute, yAttribute)
        if xAxis is None or yAxis is None:
            print("Extraction failed.")
            return
        self.ui.graphWidget.clear()    
        self.ui.graphWidget.plot(xAxis, yAxis)
        self.ui.graphWidget.autoRange()

    def display_sheet(self, csvname): #display sheet with currently selected path
        path = self.trackerEngine.getStoredPath(csvname)

        if path is None:
            print("No CSV selected.")
            return -1
        
        model = QStandardItemModel()
        self.ui.sheetWidget.setModel(model)
        self.ui.sheetWidget.horizontalHeader().setStretchLastSection(True)

        with open(path, "r", newline="", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            for i, row in enumerate(reader):
                if i == 0:
                    model.setHorizontalHeaderLabels(
                        [col.strip().strip('"') for col in row]
                    )
                else:
                    items = [QStandardItem(field.strip()) for field in row]
                    model.appendRow(items)

    def display_dual(self, csvname, xAttribute, yAttribute): #display dual-view with currently selected path
        path = self.trackerEngine.getStoredPath(csvname)
        if not path:
            print("No CSV selected.")
            return -1
        xAxis, yAxis = self.trackerEngine.extract(path, xAttribute, yAttribute)
        if xAxis is None or yAxis is None:
            print("Extraction failed.")
            return
        self.ui.graphWidgetDual.clear()    
        self.ui.graphWidgetDual.plot(xAxis, yAxis)   

        model = QStandardItemModel()
        self.ui.tableViewDual.setModel(model)
        self.ui.tableViewDual.horizontalHeader().setStretchLastSection(True)

        with open(path, "r", newline="", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            for i, row in enumerate(reader):
                if i == 0:
                    model.setHorizontalHeaderLabels(
                        [col.strip().strip('"') for col in row]
                    )
                else:
                    items = [QStandardItem(field.strip()) for field in row]
                    model.appendRow(items)           
          
    def profile_clicked(self):
        print("Profiles revealed: ")
        for i in loadProfileNames():
            print(i)

    def refreshProfileList(self):
        self.ui.profileList.clear()
        for i in self.profileEngine.profileList:
            self.ui.profileList.addItem(i)

    def openProfileWindow(self):
        print("Opening profile window")

        currentProfile = self.ui.profileList.currentIndex()

        self.profileWindow = ProfileWindow(self.profileEngine, self)
        self.profileWindow.finished.connect(
            lambda : self.closeProfileWindow(currentProfile)
        )
        self.profileWindow.exec()
        
    def closeProfileWindow(self, lastSelectedProfileIndex):

        self.ui.profileList.blockSignals(True)

        self.profileEngine.grabProfiles()
        self.refreshProfileList()
        self.ui.profileList.setCurrentIndex(lastSelectedProfileIndex)

        self.setXAttributes(self.ui.profileList.currentText())
        self.setYAttributes(self.ui.profileList.currentText())

        self.ui.profileList.blockSignals(False)

    def refreshCsvList(self):
        self.ui.csvList.clear()
        for i in self.trackerEngine.csvList:
            self.ui.csvList.addItem(str(i.name), i)

    def openCsvWindow(self):
        print("Opening csv dialog")

        self.csvWindow = CsvWindow(self.trackerEngine, self.profileEngine, self)
        self.csvWindow.finished.connect(
            lambda : self.closeCsvWindow()
        )
        self.csvWindow.exec()

    def closeCsvWindow(self):
       self.refreshCsvList()

    def setXAttributes(self, currentProfileName):
        self.ui.xAttributeBox.clear()
        for i in self.profileEngine.grabXAttributes(currentProfileName):
            self.ui.xAttributeBox.addItem(i)
            
        

    def setYAttributes(self, currentProfileName):
        self.ui.yAttributeBox.clear()
        for i in self.profileEngine.grabYAttributes(currentProfileName):
            self.ui.yAttributeBox.addItem(i)
            


    def onProfileSelected(self, selectedProfileName):

        if not selectedProfileName:
            print(f"Profile {selectedProfileName} not found")
            return

        print(f"Selected profile {selectedProfileName}")
        self.setXAttributes(selectedProfileName)
        self.setYAttributes(selectedProfileName)



