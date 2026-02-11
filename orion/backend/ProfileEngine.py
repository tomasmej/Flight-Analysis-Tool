import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog
from PySide6.QtCore import Qt
from ..ui.orion_v5 import Ui_mainWindow
from ..ui.ui_profile.profile2 import Ui_Dialog
from .database.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription, deleteProfile, getProfileXAttributes, getProfileYAttributes



class ProfileEngine:
    
    def __init__(self):
        self.profileList = []
    
    # Creates profile Default
    def createDefault(self):
        createDefaultProfile()

    # Grab all profile names from database for ui 
    def grabProfiles(self):
        for i in loadProfileNames():
            if i not in self.profileList:
                self.profileList.append(i)

    # Grab key x attributes for profile
    def grabXAttributes(self, profilename):
        x_attributes = []
        for attribute in getProfileXAttributes(profilename):
            x_attributes.append(attribute)
        return x_attributes
    
    # Grab key y attributes for profile
    def grabYAttributes(self, profilename):
        y_attributes = []
        for attribute in getProfileYAttributes(profilename):
            y_attributes.append(attribute)
        return y_attributes

    def activate(self):
        print("Profiler active")


    


   