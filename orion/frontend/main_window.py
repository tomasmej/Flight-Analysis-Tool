import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog, QFileDialog
from PySide6.QtCore import Qt
from ..ui.orion_v5 import Ui_mainWindow
from ..ui.ui_profile.profile2 import Ui_Dialog
from ..backend.TrackerEngine import TrackerEngine
from ..backend.ProfileEngine import ProfileEngine
from ..backend.database.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription
from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel, QPalette, QColor
from orion.frontend.profile_window import ProfileWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.connections()

        self.trackerEngine = TrackerEngine()
        self.refreshCsvList()

        self.profileEngine = ProfileEngine()
        createDefaultProfile()
        self.profileEngine.grabProfiles()
        self.refreshProfileList()


        # if createDefaultProfile():
        #     self.profileEngine.profileList.append(profileList[0])
        #     self.ui.profileList.addItem(profileList[0])
        #     for i in profileList:
        #         self.profileEngine.profileList.append(i)
        #         self.ui.profileList.addItem(i)

        self.ui.stackedWidget.setCurrentIndex(0)

        self.setWindowTitle("Orion")
        self.setBaseSize(800, 600)

    def connections(self):
        self.ui.importButton.clicked.connect(self.import_clicked)
        self.ui.graphButton.clicked.connect(self.graph_clicked)
        self.ui.sheetButton.clicked.connect(self.sheet_clicked)
        self.ui.resetButton.clicked.connect(self.dual_clicked)
        self.ui.profileButton.clicked.connect(self.profile_clicked)
        self.ui.configButton.clicked.connect(self.openProfileWindow)
        print('connected')

    def import_clicked(self): #import button clicked
        print('import clicked!')

        csv_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import CSV",
            "",
            "CSV Files (*.csv)"
        )

        if not csv_path:
            return


        csv_path = self.trackerEngine.addCsv(csv_path)
        print("Csv imported: " + csv_path)

        self.ui.csvList.addItem(csv_path)
        self.trackerEngine.csvList.append(csv_path)


    def graph_clicked(self): #graph button clicked
        print('Switching to graph view')       

        if self.display_graph(self.ui.csvList.currentText()) == -1:
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

        if self.display_dual(self.ui.csvList.currentText()) == -1:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.stackedWidget.setCurrentIndex(3)


    def display_graph(self, path): #display graph with currently selected path
        current_csv = path
        if not current_csv:
            print("No CSV selected.")
            return -1
        time_x, accel_y = self.trackerEngine.extract(current_csv)
        if time_x is None or accel_y is None:
            print("Extraction failed.")
            return
        self.ui.graphWidget.clear()    
        self.ui.graphWidget.plot(time_x, accel_y)

    def display_sheet(self, path): #display sheet with currently selected path
        current_csv = path
        if not current_csv:
            print("No CSV selected.")
            return -1
        
        model = QStandardItemModel()
        self.ui.sheetWidget.setModel(model)
        self.ui.sheetWidget.horizontalHeader().setStretchLastSection(True)

        with open(current_csv, "r", newline="", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            for i, row in enumerate(reader):
                if i == 0:
                    model.setHorizontalHeaderLabels(
                        [col.strip().strip('"') for col in row]
                    )
                else:
                    items = [QStandardItem(field.strip()) for field in row]
                    model.appendRow(items)

    def display_dual(self, path): #display dual-view with currently selected path
        current_csv = path
        if not current_csv:
            print("No CSV selected.")
            return -1
        time_x, accel_y = self.trackerEngine.extract(current_csv)
        if time_x is None or accel_y is None:
            print("Extraction failed.")
            return
        self.ui.graphWidgetDual.clear()    
        self.ui.graphWidgetDual.plot(time_x, accel_y)   

        model = QStandardItemModel()
        self.ui.tableViewDual.setModel(model)
        self.ui.tableViewDual.horizontalHeader().setStretchLastSection(True)

        with open(current_csv, "r", newline="", encoding="utf-8") as fileInput:
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
        
    def closeProfileWindow(self, lastSelectedProfile):
        self.profileEngine.grabProfiles()
        self.refreshProfileList()
        self.ui.profileList.setCurrentIndex(lastSelectedProfile)

    def refreshCsvList(self):
        self.ui.csvList.clear()
        for i in self.trackerEngine.getStoredCsvs():
            self.ui.csvList.addItem(str(i), i)