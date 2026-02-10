import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog
from PySide6.QtCore import Qt
from ..ui.orion_v5 import Ui_mainWindow
from ..ui.ui_profile.profile2 import Ui_Dialog
from .database.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription, deleteProfile



class ProfileEngine:
    
    def __init__(self):
        self.profileList = []
    

    def grabProfiles(self):
        for i in loadProfileNames():
            if i not in self.profileList:
                self.profileList.append(i)

    def activate(self):
        print("Profiler active")


    


   