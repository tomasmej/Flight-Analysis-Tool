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
    QListView, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.listView = QListView(csvDialog)
        self.listView.setObjectName(u"listView")

        self.centralLayout.addWidget(self.listView)

        self.csvButtons = QHBoxLayout()
        self.csvButtons.setObjectName(u"csvButtons")
        self.profileList = QPushButton(csvDialog)
        self.profileList.setObjectName(u"profileList")

        self.csvButtons.addWidget(self.profileList)

        self.comboBox = QComboBox(csvDialog)
        self.comboBox.setObjectName(u"comboBox")

        self.csvButtons.addWidget(self.comboBox)

        self.pushButton = QPushButton(csvDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.csvButtons.addWidget(self.pushButton)

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
        self.profileList.setText(QCoreApplication.translate("csvDialog", u"Import", None))
        self.pushButton.setText(QCoreApplication.translate("csvDialog", u"Delete", None))
    # retranslateUi

