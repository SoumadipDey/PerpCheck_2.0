# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facialRecogProj.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import face_recognition
import os
import json
from detailsWindow import Ui_detailsWindow

KNOWN_FACE_DIR = "img/known"
UNKNOWN_FACE_DIR = "img/unknown"
DATA_DIR = "data"

known_faces=[]
known_names=[]

data_CId = "NULL"

print("Loading known Criminal data into memory")

selectedImagePath = " "

for filename in os.listdir(KNOWN_FACE_DIR):
    image = face_recognition.load_image_file(f"{KNOWN_FACE_DIR}/{filename}")
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(filename)

print("Criminal Data Loaded into memory")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(952, 480))
        MainWindow.setMaximumSize(QtCore.QSize(952, 480))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.99)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalBaseFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalBaseFrame.setGeometry(QtCore.QRect(0, 0, 952, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalBaseFrame.sizePolicy().hasHeightForWidth())
        self.verticalBaseFrame.setSizePolicy(sizePolicy)
        self.verticalBaseFrame.setMinimumSize(QtCore.QSize(952, 480))
        self.verticalBaseFrame.setMaximumSize(QtCore.QSize(952, 480))
        self.verticalBaseFrame.setStyleSheet("background-color: rgb(130, 157, 255);\n"
        "border: 1px solid rgb(130,157,240);")
        self.verticalBaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalBaseFrame.setObjectName("verticalBaseFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalBaseFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.headingLabel = QtWidgets.QLabel(self.verticalBaseFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headingLabel.sizePolicy().hasHeightForWidth())
        self.headingLabel.setSizePolicy(sizePolicy)
        self.headingLabel.setMinimumSize(QtCore.QSize(910, 30))
        self.headingLabel.setMaximumSize(QtCore.QSize(910, 30))
        self.headingLabel.setSizeIncrement(QtCore.QSize(0, 0))
        self.headingLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(62, 56, 255);\n"
        "font: 12pt \"MS Reference Sans Serif\";\n"
        "border: 4px solid rgb(62,56,240);\n"
        "border-radius: 5px; ")
        self.headingLabel.setObjectName("headingLabel")
        self.verticalLayout.addWidget(self.headingLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalFrame = QtWidgets.QFrame(self.verticalBaseFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(930, 395))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(930, 395))
        self.horizontalFrame.setStyleSheet("")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalFrame = QtWidgets.QFrame(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(460, 394))
        self.verticalFrame.setMaximumSize(QtCore.QSize(460, 394))
        self.verticalFrame.setStyleSheet("")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectedImageLabel = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectedImageLabel.sizePolicy().hasHeightForWidth())
        self.selectedImageLabel.setSizePolicy(sizePolicy)
        self.selectedImageLabel.setMinimumSize(QtCore.QSize(300, 300))
        self.selectedImageLabel.setMaximumSize(QtCore.QSize(300, 300))
        self.selectedImageLabel.setStyleSheet("border: 1px solid rgb(93, 104, 255);")
        self.selectedImageLabel.setText("")
        self.selectedImageLabel.setPixmap(QtGui.QPixmap(":/newPrefix/baseManIcon.png"))
        self.selectedImageLabel.setScaledContents(True)
        self.selectedImageLabel.setObjectName("selectedImageLabel")
        self.verticalLayout_2.addWidget(self.selectedImageLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalFrame1 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.browseBtn = QtWidgets.QPushButton(self.horizontalFrame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtn.sizePolicy().hasHeightForWidth())
        self.browseBtn.setSizePolicy(sizePolicy)
        self.browseBtn.setMinimumSize(QtCore.QSize(200, 40))
        self.browseBtn.setMaximumSize(QtCore.QSize(200, 40))
        self.browseBtn.setStyleSheet("QPushButton {color: rgb(255, 255, 255);\n"
        "background-color: rgb(24, 124, 255);\n"
        "font: 12pt \"MS Reference Sans Serif\";\n"
        "border: 4px solid rgb(62,56,240);\n"
        "border-radius: 8px;\n"
        "text-align: center;\n"
        "}\n"
        "\n"
        "QPushButton:pressed { background-color: rgb(255, 250, 199); }\n"
        "QPushButton:hover { border-color: rgb(255, 189, 82);\n"
        "color: rgb(0,0,0);\n"
        "}\n"
        "\n"
        "")
        self.browseBtn.setObjectName("browseBtn")
        self.horizontalLayout_2.addWidget(self.browseBtn)
        
        self.browseBtn.clicked.connect(self.file_open) #connects browseBtn onClick to file_open method

        spacerItem3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.checkBtn = QtWidgets.QPushButton(self.horizontalFrame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBtn.sizePolicy().hasHeightForWidth())
        self.checkBtn.setSizePolicy(sizePolicy)
        self.checkBtn.setMinimumSize(QtCore.QSize(200, 40))
        self.checkBtn.setMaximumSize(QtCore.QSize(200, 40))
        self.checkBtn.setStyleSheet("QPushButton {color: rgb(255, 255, 255);\n"
        "background-color: rgb(24, 124, 255);\n"
        "font: 12pt \"MS Reference Sans Serif\";\n"
        "border: 4px solid rgb(62,56,240);\n"
        "border-radius: 8px;\n"
        "text-align: center;\n"
        "}\n"
        "\n"
        "QPushButton:pressed { background-color: rgb(255, 250, 199); }\n"
        "QPushButton:hover { border-color: rgb(70, 252, 10);\n"
        "color: rgb(0,0,0);\n"
        "}")
        self.checkBtn.setObjectName("checkBtn")
        self.horizontalLayout_2.addWidget(self.checkBtn)
        
        self.checkBtn.clicked.connect(self.check_function) #connects the check button to the check_fucntion

        self.verticalLayout_2.addWidget(self.horizontalFrame1)
        self.horizontalLayout.addWidget(self.verticalFrame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame_2.sizePolicy().hasHeightForWidth())
        self.verticalFrame_2.setSizePolicy(sizePolicy)
        self.verticalFrame_2.setMinimumSize(QtCore.QSize(434, 380))
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(434, 380))
        self.verticalFrame_2.setStyleSheet("border: 1px solid rgb(93, 104, 255);")
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem5)
        self.matchedImageLabel = QtWidgets.QLabel(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matchedImageLabel.sizePolicy().hasHeightForWidth())
        self.matchedImageLabel.setSizePolicy(sizePolicy)
        self.matchedImageLabel.setMinimumSize(QtCore.QSize(100, 100))
        self.matchedImageLabel.setMaximumSize(QtCore.QSize(100, 100))
        self.matchedImageLabel.setText("")
        self.matchedImageLabel.setPixmap(QtGui.QPixmap(":/newPrefix/baseManIcon.png"))
        self.matchedImageLabel.setScaledContents(True)
        self.matchedImageLabel.setObjectName("matchedImageLabel")
        self.verticalLayout_3.addWidget(self.matchedImageLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalFrame_3 = QtWidgets.QFrame(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy)
        self.horizontalFrame_3.setMinimumSize(QtCore.QSize(400, 40))
        self.horizontalFrame_3.setMaximumSize(QtCore.QSize(400, 40))
        self.horizontalFrame_3.setStyleSheet("background-color: rgb(70, 53, 255);\n"
        "border: 1px solid  rgb(70, 53, 255);\n"
        "border-radius: 6px;")
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.label_7 = QtWidgets.QLabel(self.horizontalFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255,255,255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.statusTextLabel = QtWidgets.QLabel(self.horizontalFrame_3)
        self.statusTextLabel.setMinimumSize(QtCore.QSize(25, 25))
        self.statusTextLabel.setStyleSheet("color: rgb(255,255,255);\n"
        "background-color: rgb(255, 43, 15);\n"
        "border:1px solid black;\n"
        "border-radius: 12px;")
        self.statusTextLabel.setText("")
        self.statusTextLabel.setObjectName("statusTextLabel")
        self.horizontalLayout_5.addWidget(self.statusTextLabel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_3.addWidget(self.horizontalFrame_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalFrame_4 = QtWidgets.QFrame(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_4.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_4.setSizePolicy(sizePolicy)
        self.horizontalFrame_4.setMinimumSize(QtCore.QSize(400, 40))
        self.horizontalFrame_4.setMaximumSize(QtCore.QSize(400, 40))
        self.horizontalFrame_4.setStyleSheet("background-color: rgb(70, 53, 255);\n"
        "border: 1px solid  rgb(70, 53, 255);\n"
        "border-radius: 6px;")
        self.horizontalFrame_4.setObjectName("horizontalFrame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(70, 20))
        self.label_4.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255,255,255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.nameLabel = QtWidgets.QLabel(self.horizontalFrame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setMinimumSize(QtCore.QSize(40, 20))
        self.nameLabel.setMaximumSize(QtCore.QSize(165, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color: rgb(255,255,255);")
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_6.addWidget(self.nameLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_3.addWidget(self.horizontalFrame_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(400, 40))
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(400, 40))
        self.horizontalFrame_2.setStyleSheet("background-color: rgb(70, 53, 255);\n"
        "border: 1px solid  rgb(70, 53, 255);\n"
        "border-radius: 6px;")
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.label_8 = QtWidgets.QLabel(self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.caseNumberLabel = QtWidgets.QLabel(self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.caseNumberLabel.setFont(font)
        self.caseNumberLabel.setStyleSheet("color: white;")
        self.caseNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.caseNumberLabel.setObjectName("caseNumberLabel")
        self.horizontalLayout_4.addWidget(self.caseNumberLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem12 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.openPersonFileButton = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.openPersonFileButton.setMinimumSize(QtCore.QSize(60, 25))
        self.openPersonFileButton.setMaximumSize(QtCore.QSize(60, 25))
        self.openPersonFileButton.setEnabled(False)
        self.openPersonFileButton.setStyleSheet("QPushButton {color: rgb(255, 255, 255);\n"
        "background-color: rgb(24, 124, 255);\n"
        "font: 10pt \"MS Reference Sans Serif\";\n"
        "border: 2px solid rgb(255, 187, 69);\n"
        "border-radius: 6px;\n"
        "text-align: center;\n"
        "}\n"
        "\n"
        "QPushButton:pressed { background-color: rgb(255, 250, 199); }\n"
        "QPushButton:hover { border-color: rgb(70, 252, 10);\n"
        "color: rgb(0,0,0);\n"
        "}")
        self.openPersonFileButton.setObjectName("openPersonFileButton")
        self.horizontalLayout_4.addWidget(self.openPersonFileButton, 0, QtCore.Qt.AlignTop)
        
        self.openPersonFileButton.clicked.connect(self.open_details)#connecting the button to open_details function
        
        self.verticalLayout_3.addWidget(self.horizontalFrame_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalFrame2 = QtWidgets.QFrame(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame2.setSizePolicy(sizePolicy)
        self.horizontalFrame2.setMinimumSize(QtCore.QSize(400, 50))
        self.horizontalFrame2.setMaximumSize(QtCore.QSize(400, 50))
        self.horizontalFrame2.setStyleSheet("background-color: rgb(70, 53, 255);\n"
        "border: 1px solid  rgb(70, 53, 255);\n"
        "border-radius: 6px;")
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame2)
        self.label_2.setStyleSheet("border: 0px;\n"
        "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalFrame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setStyleSheet("border: 2px solid rgb(93, 104, 255);\n"
        "color: rgb(255,255,255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_3.addWidget(self.horizontalFrame2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.verticalFrame_2)
        self.verticalLayout.addWidget(self.horizontalFrame, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def file_open(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file','c:\\', "Image files (*.jpg *.png)")
        imagePath = fname[0]
        global selectedImagePath
        #unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]
        selectedImagePath = imagePath
        pixmap = QPixmap(imagePath)
        self.selectedImageLabel.setPixmap(QPixmap(pixmap))
    
    def check_function(self): #this is the function that does it all
        #print(known_faces)
        global selectedImagePath
        #print(selectedImagePath)
        global data_CId

        unknown_image = face_recognition.load_image_file(selectedImagePath)
        face_encoding = face_recognition.face_encodings(unknown_image)[0]
        print(known_names)
        face_distances = face_recognition.face_distance(known_faces, face_encoding)
        print(face_distances)
        results = face_recognition.compare_faces(known_faces,face_encoding,tolerance=0.6)
        print(results)

        flag = False

        for value in results:
            if(value == True):
                flag = True
                
        if(flag == True): #match found
                best_match_index = np.argmin(face_distances)
                minimum_distance = face_distances[best_match_index]
                similarity_percentage = ((1-minimum_distance)/1.0)*100 
                match = known_names[best_match_index]
                data_CId = match

                matchedImagePath = f"{KNOWN_FACE_DIR}/{match}"
                pixmap = QPixmap(matchedImagePath)
                self.matchedImageLabel.setPixmap(QPixmap(pixmap))

                match=os.path.splitext(match)[0]
                self.caseNumberLabel.setText(match)
                self.statusTextLabel.setStyleSheet("color: rgb(255,255,255);\n"
                "background-color: rgb(0, 170, 0);\n"
                "border:1px solid black;\n"
                "border-radius: 12px;")
                self.progressBar.setValue(similarity_percentage)

                self.openPersonFileButton.setEnabled(True)

                with open(f"{DATA_DIR}/{match}/allData.json") as json_file:
                    data = json.load(json_file)
                    perpName = data['name']
                self.nameLabel.setText(perpName)
        else:
                self.nameLabel.setText("NULL")
                self.caseNumberLabel.setText("NULL")
                self.progressBar.setValue(0)
                self.openPersonFileButton.setEnabled(False)
                self.statusTextLabel.setStyleSheet("color: rgb(255,255,255);\n"
                "background-color: rgb(255, 43, 15);\n"
                "border:1px solid black;\n"
                "border-radius: 12px;")
                self.matchedImageLabel.setPixmap(QtGui.QPixmap(":/newPrefix/baseManIcon.png"))
    
    def open_details(self):
        #code to open the details screen here
        self.detailsWindow = QtWidgets.QMainWindow()
        self.message = data_CId
        self.ui = Ui_detailsWindow(self.message)
        self.ui.setupUi(self.detailsWindow)
        self.detailsWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PerpCheck"))
        self.headingLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Criminal Database Checker</p></body></html>"))
        self.browseBtn.setText(_translate("MainWindow", "Browse for Picture"))
        self.checkBtn.setText(_translate("MainWindow", " Check for Match "))
        self.label_7.setText(_translate("MainWindow", "Status :"))
        self.label_4.setText(_translate("MainWindow", "Full Name :"))
        self.nameLabel.setText(_translate("MainWindow", "NULL"))
        self.label_8.setText(_translate("MainWindow", "ID Number:"))
        self.caseNumberLabel.setText(_translate("MainWindow", "NULL"))
        self.openPersonFileButton.setText(_translate("MainWindow", "Open"))
        self.label_2.setText(_translate("MainWindow", "Similarity Index :"))

import resources_rc
from PyQt5.QtWidgets import QFileDialog
import numpy as np

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())