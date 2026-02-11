# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orion_v7.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.importHeader = QHBoxLayout()
        self.importHeader.setObjectName(u"importHeader")
        self.profileList = QComboBox(self.centralwidget)
        self.profileList.setObjectName(u"profileList")

        self.importHeader.addWidget(self.profileList)

        self.importButton = QPushButton(self.centralwidget)
        self.importButton.setObjectName(u"importButton")

        self.importHeader.addWidget(self.importButton)

        self.csvList = QComboBox(self.centralwidget)
        self.csvList.setObjectName(u"csvList")
        self.csvList.setEditable(True)

        self.importHeader.addWidget(self.csvList)


        self.verticalLayout_4.addLayout(self.importHeader)

        self.attributeSelectors = QHBoxLayout()
        self.attributeSelectors.setObjectName(u"attributeSelectors")
        self.xAttributeBox = QComboBox(self.centralwidget)
        self.xAttributeBox.setObjectName(u"xAttributeBox")

        self.attributeSelectors.addWidget(self.xAttributeBox)

        self.yAttributeBox = QComboBox(self.centralwidget)
        self.yAttributeBox.setObjectName(u"yAttributeBox")

        self.attributeSelectors.addWidget(self.yAttributeBox)


        self.verticalLayout_4.addLayout(self.attributeSelectors)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.empty_page = QWidget()
        self.empty_page.setObjectName(u"empty_page")
        self.stackedWidget.addWidget(self.empty_page)
        self.graph_page = QWidget()
        self.graph_page.setObjectName(u"graph_page")
        self.verticalLayout_7 = QVBoxLayout(self.graph_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graphWidget = PlotWidget(self.graph_page)
        self.graphWidget.setObjectName(u"graphWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.graphWidget)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.graph_page)
        self.sheet_page = QWidget()
        self.sheet_page.setObjectName(u"sheet_page")
        self.verticalLayout_3 = QVBoxLayout(self.sheet_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sheetWidget = QTableView(self.sheet_page)
        self.sheetWidget.setObjectName(u"sheetWidget")

        self.verticalLayout_2.addWidget(self.sheetWidget)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.sheet_page)
        self.dual_page = QWidget()
        self.dual_page.setObjectName(u"dual_page")
        self.verticalLayout_12 = QVBoxLayout(self.dual_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.graphWidgetDual = PlotWidget(self.dual_page)
        self.graphWidgetDual.setObjectName(u"graphWidgetDual")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphWidgetDual.sizePolicy().hasHeightForWidth())
        self.graphWidgetDual.setSizePolicy(sizePolicy1)
        self.graphWidgetDual.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.graphWidgetDual)

        self.tableViewDual = QTableView(self.dual_page)
        self.tableViewDual.setObjectName(u"tableViewDual")

        self.horizontalLayout_2.addWidget(self.tableViewDual)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.dual_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.viewButtons = QHBoxLayout()
        self.viewButtons.setObjectName(u"viewButtons")
        self.graphButton = QPushButton(self.centralwidget)
        self.graphButton.setObjectName(u"graphButton")

        self.viewButtons.addWidget(self.graphButton)

        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")

        self.viewButtons.addWidget(self.resetButton)

        self.sheetButton = QPushButton(self.centralwidget)
        self.sheetButton.setObjectName(u"sheetButton")

        self.viewButtons.addWidget(self.sheetButton)

        self.viewButtons.setStretch(0, 3)
        self.viewButtons.setStretch(1, 1)
        self.viewButtons.setStretch(2, 3)

        self.verticalLayout_4.addLayout(self.viewButtons)

        self.displayButtons = QHBoxLayout()
        self.displayButtons.setObjectName(u"displayButtons")
        self.configButton = QPushButton(self.centralwidget)
        self.configButton.setObjectName(u"configButton")

        self.displayButtons.addWidget(self.configButton)

        self.profileButton = QPushButton(self.centralwidget)
        self.profileButton.setObjectName(u"profileButton")

        self.displayButtons.addWidget(self.profileButton)


        self.verticalLayout_4.addLayout(self.displayButtons)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.importButton.setText(QCoreApplication.translate("mainWindow", u"Quick Import", None))
        self.csvList.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Select Data", None))
        self.graphButton.setText(QCoreApplication.translate("mainWindow", u"Graph View", None))
        self.resetButton.setText(QCoreApplication.translate("mainWindow", u"Dual View", None))
        self.sheetButton.setText(QCoreApplication.translate("mainWindow", u"Sheet View", None))
        self.configButton.setText(QCoreApplication.translate("mainWindow", u"Profiles", None))
        self.profileButton.setText(QCoreApplication.translate("mainWindow", u"CSVs", None))
    # retranslateUi

