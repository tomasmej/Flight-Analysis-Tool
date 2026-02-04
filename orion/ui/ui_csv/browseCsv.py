# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browseCsv.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_csvDialog(object):
    def setupUi(self, csvDialog):
        if not csvDialog.objectName():
            csvDialog.setObjectName(u"csvDialog")
        csvDialog.resize(900, 600)
        csvDialog.setMinimumSize(QSize(900, 600))
        self.verticalLayout_2 = QVBoxLayout(csvDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setObjectName(u"centralLayout")
        self.csvList = QListWidget(csvDialog)
        self.csvList.setObjectName(u"csvList")

        self.centralLayout.addWidget(self.csvList)

        self.csvButtons = QHBoxLayout()
        self.csvButtons.setObjectName(u"csvButtons")
        self.importButton = QPushButton(csvDialog)
        self.importButton.setObjectName(u"importButton")

        self.csvButtons.addWidget(self.importButton)

        self.profileBox = QComboBox(csvDialog)
        self.profileBox.setObjectName(u"profileBox")

        self.csvButtons.addWidget(self.profileBox)

        self.deleteButton = QPushButton(csvDialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.csvButtons.addWidget(self.deleteButton)

        self.csvButtons.setStretch(0, 1)
        self.csvButtons.setStretch(1, 2)
        self.csvButtons.setStretch(2, 1)

        self.centralLayout.addLayout(self.csvButtons)


        self.verticalLayout_2.addLayout(self.centralLayout)


        self.retranslateUi(csvDialog)

        QMetaObject.connectSlotsByName(csvDialog)
    # setupUi

    def retranslateUi(self, csvDialog):
        csvDialog.setWindowTitle(QCoreApplication.translate("csvDialog", u"Dialog", None))
        self.importButton.setText(QCoreApplication.translate("csvDialog", u"Import", None))
        self.deleteButton.setText(QCoreApplication.translate("csvDialog", u"Delete", None))
    # retranslateUi

