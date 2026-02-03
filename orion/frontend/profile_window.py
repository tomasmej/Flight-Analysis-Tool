import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog, QInputDialog, QLineEdit
from PySide6.QtCore import Qt
from ..ui.orion_v6 import Ui_mainWindow
from ..ui.ui_profile.profile3 import Ui_Dialog
# from ..backend.TrackerEngine import TrackerEngine
# from ..backend.ProfileEngine import ProfileEngine
from ..backend.database.database import *
from orion.frontend.new_profile_dialog import NewProfileDialog


class ProfileWindow(QDialog):
    def __init__(self, profileEngine, parent=None):
        super().__init__(parent)

        self.engine = profileEngine
        self.engine.activate()
    

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.connections()
        self.refreshProfileList()

        self.setWindowTitle("Configuration")
        self.setBaseSize(500, 660)

        self.ui.editBox.setDisabled(True)


    def connections(self):
            self.ui.profileList.itemClicked.connect(self.onItemClicked)
            self.ui.newProfileButton.clicked.connect(self.newProfileClicked)
            self.ui.deleteProfileButton.clicked.connect(self.deleteClicked)

            self.ui.editProfileButton.clicked.connect(
                lambda: self.editClicked(self.ui.profileList.selectedItems()[0])
            )

            self.ui.newAttribute.clicked.connect(self.newXAttributeClicked)
            self.ui.deleteAttribute.clicked.connect(self.deleteXAttributeClicked)

            self.ui.newAttribute_2.clicked.connect(self.newYAttributeClicked)
            self.ui.deleteAttribute_2.clicked.connect(self.deleteYAttributeClicked)

            self.ui.confirmButton.clicked.connect(self.editConfirmed)



    def refreshProfileList(self):
        self.ui.profileList.clear()
        for i in loadProfileNames():
            self.ui.profileList.addItem(i)

    def onItemClicked(self, item):
        profileName = item.text()
        print("Clicked profile:", profileName)
        self.ui.descriptionBox.setPlainText(getProfileDescription(profileName))

        self.refreshXAttributes(profileName)
        self.refreshYAttributes(profileName)

    def newProfileClicked(self):
        self.newProfileDialogue = NewProfileDialog()
        self.newProfileDialogue.exec()
        self.refreshProfileList()
        
    def deleteClicked(self):
        profileName = self.ui.profileList.currentItem().text()
        print("Profile to delete:", profileName)
        deleteProfile(profileName)
        self.refreshProfileList()
        self.ui.descriptionBox.clear()



    def editClicked(self, item):
         print("Editing profile: ", item.text())
         self.ui.editBox.setDisabled(False)
         self.ui.profileBox.setDisabled(True)
        #  self.ui.editBox.objectName = item.text()


    def editConfirmed(self):
         self.ui.editBox.setDisabled(True)
         self.ui.profileBox.setDisabled(False)
         
    def refreshXAttributes(self, profileName):
         self.ui.attributeList.clear()
         for i in getProfileXAttributes(profileName):
            self.ui.attributeList.addItem(i)

    def refreshYAttributes(self, profileName):
         self.ui.attributeList_2.clear()
         for i in getProfileYAttributes(profileName):
            self.ui.attributeList_2.addItem(i)


    def newXAttributeClicked(self):
        # Open text input dialog
        text, ok = QInputDialog.getText(
            self,
            "Input Dialog",           # Dialog title
            "Enter your text:",       # Label inside the dialog
            QLineEdit.Normal,         # Input mode
            ""                        # Default text
        )

        if ok and text:
            addXAttribute(self.ui.profileList.currentItem().text(), text)

        self.refreshXAttributes(self.ui.profileList.currentItem().text())

    def deleteXAttributeClicked(self):
            deleteXAttribute(self.ui.profileList.currentItem().text(), self.ui.attributeList.currentItem().text())
            self.refreshXAttributes(self.ui.profileList.currentItem().text())

    def newYAttributeClicked(self):
        # Open text input dialog
        text, ok = QInputDialog.getText(
            self,
            "Input Dialog",           # Dialog title
            "Enter your text:",       # Label inside the dialog
            QLineEdit.Normal,         # Input mode
            ""                        # Default text
        )

        if ok and text:
            addYAttribute(self.ui.profileList.currentItem().text(), text)

        self.refreshYAttributes(self.ui.profileList.currentItem().text())

    def deleteYAttributeClicked(self):
            deleteYAttribute(self.ui.profileList.currentItem().text(), self.ui.attributeList_2.currentItem().text())
            self.refreshYAttributes(self.ui.profileList.currentItem().text())


    # def dialogEnd(self, result):
    #     if result == QDialog.Accepted:
    #         self.engine.save_profile()