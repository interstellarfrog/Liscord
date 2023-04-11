from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import requests
import threading
import socket
import rsa

# IMPORTANT! You need pillow package for screenshare

import time as T
from vidstream import ScreenShareClient, AudioReceiver, AudioSender, StreamingServer
global Target, publicIp, privateIp, Connected, Hosting, connectingToHost, otherPersonStreaming, fullText, screenShareOn, setText, IpSet, UserNameSet, TargetSet, incomingCall, notJoining, inCall, directory, publicPartner, publicKey, privateKey
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket connection
hostName = socket.gethostname()  # gets host name
publicIp = requests.get('https://api.ipify.org/').text  # gets public ip
privateIp = socket.gethostbyname(hostName)  # gets private ip of host name
Hosting = False
connectingToHost = False
Connected = False
UserNameSet = False
IpSet = False
TargetType = ""
TargetSet = False
IpType = ""
error = False
PORT = 55555
fullText = ("C͟H͟A͟T͟")
setText = False
incomingCall = False
screenShareOn = False
otherPersonStreaming = False
notJoining = False
inCall = False
directory = os.getcwd()
publicKey, privateKey = rsa.newkeys(1024)
publicPartner = None
Target = ""


'''
GUI
'''


##################################################################################################################################################
class Ui_Liscord(object):
    def setupUi(self, Liscord):
        Liscord.setWindowIcon(QtGui.QIcon(
            str(directory) + "\\LiscordFlat.png"))
        Liscord.setObjectName("Liscord")
        Liscord.resize(850, 657)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        Liscord.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Liscord.setFont(font)
        Liscord.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Liscord.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Liscord.setWindowIcon(icon)
        Liscord.setAutoFillBackground(False)
        Liscord.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                              "")
        self.centralwidget = QtWidgets.QWidget(Liscord)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setStyleSheet("color: rgb(0, 0, 127);")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LiscordTitle = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.LiscordTitle.setFont(font)
        self.LiscordTitle.setMouseTracking(False)
        self.LiscordTitle.setStyleSheet("color:rgb(0, 0, 127)")
        self.LiscordTitle.setScaledContents(True)
        self.LiscordTitle.setObjectName("LiscordTitle")
        self.verticalLayout_2.addWidget(self.LiscordTitle)
        self.line = QtWidgets.QFrame(self.widget_6)
        self.line.setStyleSheet("color:rgb(0, 0, 127);\n"
                                "background-color:rgb(0, 0, 127);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(
            258, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.IPTitle = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.IPTitle.setFont(font)
        self.IPTitle.setWordWrap(True)
        self.IPTitle.setObjectName("IPTitle")
        self.verticalLayout_2.addWidget(self.IPTitle)
        self.hostIPBox = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hostIPBox.setFont(font)
        self.hostIPBox.setStyleSheet("color: rgb(0, 0, 127);\n"
                                     "")
        self.hostIPBox.setText("")
        self.hostIPBox.setObjectName("hostIPBox")
        self.verticalLayout_2.addWidget(self.hostIPBox)
        self.pushButton = QtWidgets.QPushButton(self.widget_6)
        self.pushButton.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.targetTitle = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.targetTitle.setFont(font)
        self.targetTitle.setObjectName("targetTitle")
        self.verticalLayout_2.addWidget(self.targetTitle)
        self.targetIPBox = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.targetIPBox.setFont(font)
        self.targetIPBox.setStyleSheet("color: rgb(0, 0, 127);\n"
                                       "")
        self.targetIPBox.setInputMask("")
        self.targetIPBox.setText("")
        self.targetIPBox.setObjectName("targetIPBox")
        self.verticalLayout_2.addWidget(self.targetIPBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_2.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)

        self.HostButton = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        self.HostButton.setText("HOST")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.HostButton.setFont(font)
        self.HostButton.setStyleSheet("background-color: rgb(17, 17, 17);\n"
                                      "color: rgb(0, 0, 125);\n"
                                      "")
        self.HostButton.setObjectName("HostButton")
        self.HostButton.setToolTip("Press To Host Connection")
        self.verticalLayout_2.addWidget(self.HostButton)

        palette = QtGui.QPalette()
        self.HostButton.setPalette(palette)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        self.HostButton.setPalette(palette)

        self.Connect_button = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.Connect_button.setFont(font)
        self.Connect_button.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.Connect_button.setObjectName("Connect_button")
        self.verticalLayout_2.addWidget(self.Connect_button)

        self.Disconnect = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Disconnect.setFont(font)
        self.Disconnect.setStyleSheet("color: rgb(140, 0, 0);\n"
                                      "background-color: rgb(17, 17, 17);\n"
                                      "")
        self.Disconnect.setObjectName("Disconnect")
        self.verticalLayout_2.addWidget(self.Disconnect)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.startVoip = QtWidgets.QPushButton(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.startVoip.setFont(font)
        self.startVoip.setStyleSheet("background-color: rgb(17, 17, 17);\n"
                                     "color: rgb(0, 0, 127);")
        self.startVoip.setObjectName("startVoip")
        self.verticalLayout.addWidget(self.startVoip)
        self.screenShare = QtWidgets.QPushButton(self.widget_8)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.screenShare.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.screenShare.setFont(font)
        self.screenShare.setMouseTracking(False)
        self.screenShare.setStyleSheet("background-color: rgb(17, 17, 17);\n"
                                       "color:rgb(0, 0, 127);\n"
                                       "\n"
                                       "")
        self.screenShare.setAutoExclusive(False)
        self.screenShare.setObjectName("screenShare")
        self.verticalLayout.addWidget(self.screenShare)
        self.helpButton = QtWidgets.QPushButton(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(37)
        self.helpButton.setFont(font)
        self.helpButton.setStyleSheet("color: rgb(0, 0, 127);\n"
                                      "background-color: rgb(17, 17, 17);\n"
                                      "")
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout.addWidget(self.helpButton)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_3.addWidget(self.widget_8)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.timeLabel = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color:rgb(255, 255, 255);\n"
                                     "background-color: rgb(17, 17, 17);")
        self.timeLabel.setText("")
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout_4.addWidget(self.timeLabel)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.USERNAMETitle = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.USERNAMETitle.setFont(font)
        self.USERNAMETitle.setStyleSheet("color:rgb(0, 0, 127)")
        self.USERNAMETitle.setObjectName("USERNAMETitle")
        self.horizontalLayout_2.addWidget(self.USERNAMETitle)
        self.usernameBox = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        self.usernameBox.setFont(font)
        self.usernameBox.setStyleSheet("color:rgb(0, 0, 127)")
        self.usernameBox.setText("")
        self.usernameBox.setObjectName("usernameBox")
        self.horizontalLayout_2.addWidget(self.usernameBox)
        self.usernameButton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.usernameButton.setFont(font)
        self.usernameButton.setStyleSheet("color:rgb(0, 0, 127);\n"
                                          "background-color: rgb(17, 17, 17);")
        self.usernameButton.setObjectName("usernameButton")
        self.horizontalLayout_2.addWidget(self.usernameButton)
        self.usernameButton.raise_()
        self.usernameBox.raise_()
        self.USERNAMETitle.raise_()
        self.verticalLayout_4.addWidget(self.widget_2)
        self.chatBox = QtWidgets.QTextBrowser(self.widget_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.chatBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.chatBox.setFont(font)
        self.chatBox.setStyleSheet("")
        self.chatBox.setOpenExternalLinks(False)
        self.chatBox.setObjectName("chatBox")
        self.verticalLayout_4.addWidget(self.chatBox)
        self.widget = QtWidgets.QWidget(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBox = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBox.setFont(font)
        self.textBox.setAutoFillBackground(False)
        self.textBox.setStyleSheet("color: rgb(0, 0, 127);")
        self.textBox.setText("")
        self.textBox.setObjectName("textBox")
        self.horizontalLayout.addWidget(self.textBox)
        self.enterText = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.enterText.setFont(font)
        self.enterText.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.enterText.setAutoFillBackground(False)
        self.enterText.setStyleSheet("color:rgb(0, 0, 127);\n"
                                     "background-color: rgb(17, 17, 17);")
        self.enterText.setObjectName("enterText")
        self.horizontalLayout.addWidget(self.enterText)
        self.verticalLayout_4.addWidget(self.widget)
        self.horizontalLayout_3.addWidget(self.widget_3)
        Liscord.setCentralWidget(self.centralwidget)

        self.retranslateUi(Liscord)
        QtCore.QMetaObject.connectSlotsByName(Liscord)

    def retranslateUi(self, Liscord):
        _translate = QtCore.QCoreApplication.translate
        Liscord.setWindowTitle(_translate("Liscord", "Liscord"))
        self.LiscordTitle.setText(_translate("Liscord", "Liscord"))
        self.IPTitle.setText(_translate("Liscord", "Enter Your IP"))
        self.hostIPBox.setPlaceholderText(_translate("Liscord", "Host"))
        self.pushButton.setToolTip(_translate("Liscord", "Confirm"))
        self.pushButton.setText(_translate("Liscord", "CONFIRM"))
        self.targetTitle.setText(_translate("Liscord", "Enter Target IP"))
        self.targetIPBox.setPlaceholderText(_translate("Liscord", "Connect"))
        self.pushButton_2.setToolTip(_translate("Liscord", "Confirm"))
        self.pushButton_2.setText(_translate("Liscord", "CONFIRM"))
        self.Connect_button.setToolTip(_translate(
            "Liscord", "<html><head/><body><p>Connects to target ip with your ip</p></body></html>"))
        self.Connect_button.setText(_translate("Liscord", "Connect"))
        self.Disconnect.setToolTip(_translate(
            "Liscord", "Disconnect from everything"))
        self.Disconnect.setText(_translate("Liscord", "Disconnect"))
        self.startVoip.setToolTip(_translate(
            "Liscord", "Start a call with other members of the chat"))
        self.startVoip.setText(_translate("Liscord", "Call"))
        self.screenShare.setToolTip(_translate(
            "Liscord", "<html><head/><body><p>Show your screen to other members of the chat</p></body></html>"))
        self.screenShare.setText(_translate("Liscord", "screen share"))
        self.helpButton.setToolTip(_translate(
            "Liscord", "Click if you dont know what you are doing"))
        self.helpButton.setText(_translate("Liscord", "Help!"))
        self.USERNAMETitle.setText(_translate("Liscord", "USERNAME"))
        self.usernameButton.setToolTip(_translate("Liscord", "Enter"))
        self.usernameButton.setText(_translate("Liscord", "⏎"))
        self.chatBox.setHtml(_translate("Liscord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#ff0000;\">CHAT</span></p></body></html>"))
        self.textBox.setPlaceholderText(
            _translate("Liscord", "Start Chatting!"))
        self.enterText.setToolTip(_translate("Liscord", "Enter"))
        self.enterText.setText(_translate("Liscord", "⏎"))
##############################################################################################################################################################################################

        '''
        
        buttons
        '''

        self.helpButton.clicked.connect(self.help)  # if Help button pressed
        # if enter my ip button pressed
        self.pushButton_2.clicked.connect(self.targetClicked)
        # if target ip button pressed
        self.pushButton.clicked.connect(self.ipClicked)
        self.usernameButton.clicked.connect(
            self.usernameClicked)  # if username button pressed
        self.Connect_button.clicked.connect(
            self.connect)  # if connect button pressed
        self.HostButton.clicked.connect(self.Host)  # if host button pressed
        # if enter text button pressed
        self.enterText.clicked.connect(self.sendButtonClicked)
        # if disconnect button pressed
        self.Disconnect.clicked.connect(self.disconnect)
        self.startVoip.clicked.connect(self.voip)  # if call button pressed
        # if screen share button pressed
        self.screenShare.clicked.connect(self.screen_Share)

    def screen_Share(self):  # if screen share button pressed
        global Connected, screenShareOn, sender, Hosting, Client, connectingToHost, ScreenShareClient, screenShareThread, conn, otherPersonStreaming, audioRecver1, audioSend1, audiorecver2, audioSend2, publicPartner
        if Connected:
            if otherPersonStreaming:
                sender = ScreenShareClient(IP, 9998)
            else:
                sender = ScreenShareClient(IP, 9999)
            if screenShareOn == False:  # if screenShareOn not on
                screenShareOn = True
                screenshareThread = threading.Thread(
                    target=sender.start_stream)
                if Hosting:
                    conn.send(rsa.encrypt("!STARTING_SCREEN_SHARE!".encode(
                        "utf-8"), publicPartner))  # send encrypted and encoded text
                elif connectingToHost:
                    Client.send(rsa.encrypt("!STARTING_SCREEN_SHARE!".encode(
                        "utf-8"), publicPartner))  # send encrypted and encoded text
                screenshareThread.start()
            else:
                if Hosting:
                    # send encrypted and encoded text
                    conn.send(rsa.encrypt(
                        "!STOP_SHARE_SCREEN!".encode("utf-8"), publicPartner))
                    screenShareOn = False
                elif connectingToHost:
                    # send encrypted and encoded text
                    Client.send(rsa.encrypt(
                        "!STOP_SHARE_SCREEN!".encode("utf-8"), publicPartner))
                    screenShareOn = False
        else:
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("ScreenShare")  # ScreenShare menu title
            # ScreenShare window text
            msg.setText("You Need To Be Connected To ScreenShare")
            # shows ! mark when ScreenShare window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box

    def voip(self):
        global Connected, Hosting, inCall, publicPartner
        if Connected == False:
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("VOIP")  # VOIP menu title
            # VOIP window text
            msg.setText("You Need To Be Connected To Call Someone")
            # shows ! mark when VOIP window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
        else:
            if inCall:
                if Hosting:
                    audioRecver1.stop_server()
                    audioSend1.stop_stream()
                elif connectingToHost:
                    audioRecver2.stop_server()
                    audioSend2.stop_stream()
                inCall = False
            else:
                if Hosting:
                    # send encrypted and encoded text
                    conn.send(rsa.encrypt(
                        "!INCOMING_CALL!".encode("utf-8"), publicPartner))
                elif connectingToHost:
                    # send encrypted and encoded text
                    Client.send(rsa.encrypt(
                        "!INCOMING_CALL!".encode("utf-8"), publicPartner))

    def disconnect(self):
        global Connected, conn, Host, fullText, sendButtonClicked, Hosting, connectingToHost, publicPartner
        print("Disconnect pressed")
        if Connected:
            if Hosting:
                # send encrypted and encoded text
                conn.send(rsa.encrypt(
                    "!LEAVINGTHECHAT!".encode("utf-8"), publicPartner))
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                Host.close()
                Connected = False
                fullText = fullText + "\n You Have Left The Chat"
                sendButtonClicked = True
                Hosting = False
                connectingToHost = False
            elif connectingToHost:
                # send encrypted and encoded text
                Client.send(rsa.encrypt(
                    "!LEAVINGTHECHAT!".encode("utf-8"), publicPartner))
                Client.shutdown(socket.SHUT_RDWR)
                Client.close()
                Connected = False
                fullText = fullText + "\n You Have Left The Chat"
                sendButtonClicked = True
                Hosting = False
                connectingToHost = False

        else:
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Disconnect")  # Disconnect menu title
            # Disconnect window text
            msg.setText("You Need To Be Connected To Disconnect")
            # shows ! mark when Disconnect window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box

    def updateChatBox(self):
        global sendButtonClicked, incomingCall, Hosting, connectingToHost, notJoining, inCall, audioRecver2, audioSend2, publicPartner
        sendButtonClicked = False
        while True:
            QtCore.QCoreApplication.processEvents()  # so gui doesnt freeze
            if sendButtonClicked:
                print("updated chat box")
                self.chatBox.setText(fullText)
                sendButtonClicked = False
            elif incomingCall:
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("INCOMING CALL!")  # menu title
                msg.setText("Do You Want To Join The Call?")  # window text
                # shows information mark when window opened
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                x = msg.exec_()  # activates message box
                if x == QMessageBox.Ok:
                    if Hosting:
                        # send encrypted and encoded text
                        conn.send(rsa.encrypt(
                            "!JOINING_CALL!".encode("utf-8"), publicPartner))
                        audioRecver2 = AudioReceiver(IP, 15568)
                        audiorecverThread2 = threading.Thread(
                            target=audioRecver2.start_server)
                        audioSend2 = AudioSender(IP, 15567)
                        audioSendThread2 = threading.Thread(
                            target=audioSend2.start_stream)
                        audiorecverThread2.start()
                        audioSendThread2.start()
                        inCall = True
                    elif connectingToHost:
                        # send encrypted and encoded text
                        Client.send(rsa.encrypt(
                            "!JOINING_CALL!".encode("utf-8"), publicPartner))
                        audioRecver2 = AudioReceiver(IP, 15568)
                        audiorecverThread2 = threading.Thread(
                            target=audioRecver2.start_server)
                        audioSend2 = AudioSender(IP, 15567)
                        audioSendThread2 = threading.Thread(
                            target=audioSend2.start_stream)
                        audiorecverThread2.start()
                        audioSendThread2.start()
                        inCall = True
                elif x == QMessageBox.Cancel:
                    if Hosting:
                        conn.send(rsa.encrypt(
                            "!NOT_JOINING!".encode("utf-8"), publicPartner))
                    elif connectingToHost:
                        Client.send(rsa.encrypt(
                            "!NOT_JOINING!".encode("utf-8"), publicPartner))
                incomingCall = False
            elif notJoining:
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Call")  # menu title
                # window text
                msg.setText("The Other Person Refused The Call ")
                # shows ! mark when window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()
                notJoining = False

            else:
                pass

    def Host(self):
        global Connected, UserNameSet, IpSet, TargetSet, Host, privateKey, publicPartner
        if Connected:  # if connected
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Host")  # Host menu title
            # Host window text
            msg.setText("You Are Already Connected To Someone")
            # shows ! mark when Host window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
        else:  # if not connected
            if UserNameSet == False:
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Username")  # menu title
                msg.setText("You Need To Add your Username ")  # window text
                # shows ! mark when window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # activates message box
            elif IpSet == False:
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Your IP")  # menu title
                msg.setText("You Need To Add your IP ")  # window text
                # shows ! mark when window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # activates message box
            else:
                Host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    Host.bind((IP, PORT))
                    hostIpError = False
                except:
                    hostIpError = True

                if hostIpError:
                    msg = QMessageBox()  # makes message box
                    msg.setWindowTitle("Host IP")  # menu title
                    msg.setText("Your Host IP Is Invalid ")  # window text
                    # shows ! mark when window opened
                    msg.setIcon(QMessageBox.Critical)
                    x = msg.exec_()  # activates message box
                else:
                    Host.listen(1)  # listens for anyone trying to connect
                    print("Waiting for connection on port " + str(PORT))
                    global conn, addr, ClientUsername, fullText, Hosting
                    Host.settimeout(1)
                    accepting = True
                    hostAcceptingCount = 0
                    while accepting:
                        try:
                            conn, addr = Host.accept()  # accepts whoever trys to connect
                            print("connection accepted")
                            hostAcceptingError = False  # no error
                            accepting = False  # stop looping
                        except:
                            QtCore.QCoreApplication.processEvents()  # stops gui from freezing
                            hostAcceptingCount = hostAcceptingCount + 1
                            if hostAcceptingCount == 30:
                                hostAcceptingError = True  # error
                                accepting = False  # stop looping

                    if hostAcceptingError:
                        msg = QMessageBox()  # makes message box
                        msg.setWindowTitle("Host Connection")  # menu title
                        # window text
                        msg.setText(
                            "No One Connected To You So We Closed The Connection ")
                        # shows ! mark when window opened
                        msg.setIcon(QMessageBox.Critical)
                        x = msg.exec_()  # activates message box
                    else:
                        T.sleep(1)
                        conn.send(publicKey.save_pkcs1("PEM"))
                        publicPartner = rsa.PublicKey.load_pkcs1(
                            conn.recv(1024))
                        ClientUsername = rsa.decrypt(
                            conn.recv(1024), privateKey).decode("utf-8")
                        T.sleep(0.5)
                        conn.send(rsa.encrypt(
                            str(myUserName).encode("utf-8"), publicPartner))
                        print("connected with " + str(ClientUsername))
                        fullText = str(fullText) + \
                            "\nCONNECTED WITH " + str(ClientUsername)
                        self.chatBox.setText(str(fullText))
                        Connected = True
                        Hosting = True
                        t1 = threading.Thread(target=self.receiving1)
                        t2 = threading.Thread(target=self.sending1)
                        t1.daemon = True
                        t2.daemon = True
                        t1.start()
                        t2.start()
                        self.updateChatBox()

    def receiving1(self):
        global fullText, ClientUsername, sendButtonClicked, conn, receiver, privateKey, otherPersonStreaming, screenShareOn, Connected, Hosting, connectingToHost, incomingCall, notJoining, inCall, audioRecver1, audioSend1
        sendButtonClicked = False
        while True:
            try:
                if Connected == False:
                    break
                message = rsa.decrypt(conn.recv(1024), privateKey).decode(
                    "utf-8")  # receive message decrpt and decode
                if message == "!LEAVINGTHECHAT!":  # if leaving chat message received
                    fullText = str(fullText) + "\n" + \
                        str(ClientUsername) + " Has Left The Chat"
                    print(str(fullText))
                    Hosting = False
                    connectingToHost = False
                    Connected = False
                    sendButtonClicked = True  # set text
                    # shutdown read and write on the socket
                    conn.shutdown(socket.SHUT_RDWR)
                    conn.close()  # close socket
                elif message == "!STOP_SHARE_SCREEN!":  # if stop shar screen message received
                    fullText = str(fullText) + "\nSTOPING SHARESCREEN"
                    sendButtonClicked = True  # set text
                    try:
                        receiver.stop_server()  # stop screen share
                        otherPersonStreaming = False
                    except:
                        pass
                elif message == "!STARTING_SCREEN_SHARE!":
                    if screenShareOn:
                        receiver = StreamingServer(IP, 9998)
                        print("starting port 9998 " +
                              str(otherPersonStreaming))
                    else:
                        receiver = StreamingServer(IP, 9999)
                        print("starting port 9999")
                    screenShareThread = threading.Thread(
                        target=receiver.start_server)
                    screenShareThread.start()
                    otherPersonStreaming = True
                elif message == "!INCOMING_CALL!":
                    incomingCall = True
                elif message == "!NOT_JOINING!":
                    notJoining = True
                elif message == "!JOINING_CALL!":
                    audioRecver1 = AudioReceiver(IP, 15567)
                    audiorecverThread1 = threading.Thread(
                        target=audioRecver1.start_server)
                    audioSend1 = AudioSender(IP, 15568)
                    audioSendThread1 = threading.Thread(
                        target=audioSend1.start_stream)
                    audiorecverThread1.start()
                    audioSendThread1.start()
                    inCall = True
                else:
                    fullText = str(fullText) + "\n" + \
                        str(ClientUsername) + "->" + str(message)
                    print("received message setting text box")
                    sendButtonClicked = True
            except:
                pass

    def sending1(self):
        global sendButtonClicked2, fullText, conn, Connected, publicPartner
        sendButtonClicked2 = False
        while True:
            if Connected == False:
                break
            if sendButtonClicked2:
                # get message from text box
                message = str(self.textBox.text())
                print("sending message")
                conn.send(rsa.encrypt(
                    message.encode("utf-8"), publicPartner))
                fullText = fullText + "\n" + \
                    str(myUserName) + "->" + str(message)
                print("setting text")
                sendButtonClicked2 = False
            else:
                pass

    def sendButtonClicked(self):

        print("send button clicked")
        global sendButtonClicked, sendButtonClicked2
        sendButtonClicked = True
        sendButtonClicked2 = True
        T.sleep(0.3)
        self.textBox.setText("")  # set textbox back to blank

    def usernameClicked(self):
        # get username from username box
        global myUserName
        myUserName = self.usernameBox.text()
        print("USERNAME = " + "(" + str(myUserName) + ")")
        userNameLength = len(myUserName)
        if userNameLength > 12 or userNameLength < 3:
            myUserName = ""
            global UserNameSet
            UserNameSet = False
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Username")  # help menu title
            # help window text
            msg.setText(
                "UserName cant be less than 3 characters or more than 12 characters")
            # shows question mark when help window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
        # getting out invisible letters
        elif 'ㅤ' in myUserName or '	' in myUserName or ' ' in myUserName or ' ' in myUserName or '͏͏­­­­­؜­' in myUserName or 'ᅟ' in myUserName or 'ᅟ' in myUserName or 'ᅠ' in myUserName or '឵᠎᠎ ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or '‎​​‌' in myUserName or '‏' in myUserName or ' ' in myUserName or ' ' in myUserName or ' ' in myUserName or '　⁯⁭⁮⁣' in myUserName or '　' in myUserName or '⠀' in myUserName or 'ㅤ' in myUserName or '﻿' in myUserName or 'ﾠ' in myUserName or '𝅙' in myUserName:
            myUserName = ""
            UserNameSet = False
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Username")  # menu title
            msg.setText("NO invisible characters allowed")  # window text
            # shows ! mark when window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
        elif " " in myUserName:
            myUserName = ""
            UserNameSet = False
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Username")  # menu title
            msg.setText("NO spaces allowed")  # window text
            # shows ! when help window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
        elif myUserName == "":
            UserNameSet = False
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Username")  # menu title
            msg.setText("You must have a UserName")  # window text
            # shows ! mark when help window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
        else:
            UserNameSet = True
            print(UserNameSet)
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Username")  # help menu title
            # help window text
            msg.setText("UserName set as " + str(myUserName))
            # shows question mark when help window opened
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()  # activates message box
            return myUserName, UserNameSet

        return myUserName, UserNameSet

    def targetClicked(self):
        # get ip from target box

        error = False
        global Target
        Target = self.targetIPBox.text()
        if " " in Target:  # if space in ip
            Target = ""
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Target")  # menu title
            # window text
            msg.setText("There is a space inside your Target IP")
            # shows ! mark when help window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
            global TargetSet
            TargetSet = False

        elif Target == "":
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Target")  # menu title
            msg.setText("You must add Your Target IP")  # window text
            # shows ! mark when help window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
            TargetSet = False
        else:
            TargetType = ""
            if "." in Target:
                intcheck = Target.split(".")
                if " " in intcheck:
                    intcheck.remove(" ")
                if "" in intcheck:
                    intcheck.remove("")
                a = len(intcheck)
                num = 0
                chekingInt = True
                while chekingInt:
                    error = False
                    number = intcheck[num]
                    try:
                        int(number)
                        if num == a - 1:
                            chekingInt = False
                            TargetType = "Ipv4"
                            print(TargetType)
                        else:
                            num = num + 1
                    except:
                        chekingInt = False
                        print("Target invalid")
                        msg = QMessageBox()  # makes message box
                        msg.setWindowTitle("Target")  # menu title
                        # window text
                        msg.setText(
                            "Invalid Target ipv4 Must be numbers only no letters")
                        # shows ! mark when help window opened
                        msg.setIcon(QMessageBox.Critical)
                        x = msg.exec_()  # activates message box
                        error = True

            if ":" in Target and TargetType == "" and error == False:
                TargetType = "Ipv6"
            if TargetType == "" and error == False:
                Target = ""
                print("Target invalid")
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Target")  # menu title
                msg.setText("Invalid Target")  # window text
                # shows ! mark when help window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # activates message box
            elif error == False:
                print("Target IP = " + "(" + str(Target) +
                      ") IP type = " + str(TargetType))
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Target")  # menu title
                msg.setText("Your Target IP is " + "(" + str(Target) +
                            ") IP type = " + str(TargetType))  # window text
                # shows ! mark when help window opened
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()  # activates message box
                TargetSet = True
                return TargetType, TargetSet

        return Target

    def help(self):
        # display help message
        msg = QMessageBox()  # makes message box
        msg.setWindowTitle("Help Menu")  # help menu title
        msg.setText("1.Enter your username and click enter\n2.Set your ip for host and your ip and target IP to connect to a host (works on both on network and off network for connecting off network use the other computers public IP address and to host use private ip) you can get private ip from typing ipconfig in cmd and public from searching on google 'What is my ip' \n3.Press host to host a chat and connect to connect to a host\n4.Once connected you can use the chat, voice call and screenshare\nYou can hover over buttons to get more info\nIf the program breaks just restart it- normally breaks when screensharing or calling more than once")  # help window text
        # shows question mark when help window opened
        msg.setIcon(QMessageBox.Question)
        x = msg.exec_()  # activates message box

    def ipClicked(self):
        # if confirm ip clicked
        global IP
        IP = self.hostIPBox.text()
        error2 = False

        if " " in IP:  # if space in ip
            IP = ""
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("IP")  # menu title
            msg.setText("There is a space inside your IP")  # window text
            # shows ! mark when help window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
            global IpSet
            IpSet = False
        elif IP == "":
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("IP")  # menu title
            msg.setText("You must add Your IP")  # window text
            # shows ! mark when help window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
            IpSet = False

        else:
            IpType = ""
            if "." in IP:  # checks for Ipv4
                intcheck = IP.split(".")
                if " " in intcheck:
                    intcheck.remove(" ")
                if "" in intcheck:
                    intcheck.remove("")
                a = len(intcheck)
                num = 0
                chekingInt = True
                while chekingInt:  # checks for int
                    error2 = False
                    number = intcheck[num]
                    try:
                        int(number)
                        if num == a - 1:
                            chekingInt = False
                            IpType = "Ipv4"
                            print(IpType)
                        else:
                            num = num + 1
                    except:
                        chekingInt = False
                        print("Your IP is invalid")
                        msg = QMessageBox()  # makes message box
                        msg.setWindowTitle("Target")  # menu title
                        # window text
                        msg.setText(
                            "Invalid IP Ipv4 Must be numbers only no letters")
                        # shows ! mark when help window opened
                        msg.setIcon(QMessageBox.Critical)
                        x = msg.exec_()  # activates message box
                        error2 = True  # sets it as error so it skips the rest of the function

            if ":" in IP and IpType == "" and error2 == False:
                IpType = "Ipv6"
            if IpType == "" and error2 == False:
                IP = ""
                print("target invalid")
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Your IP")  # menu title
                msg.setText("Invalid IP")  # window text
                # shows ! mark when help window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # activates message box
            elif error2 == False:
                print("Your IP = " + "(" + str(IP) + ") IP type = " + str(IpType))
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("IP")  # menu title
                msg.setText("Your ip is " + "(" + str(IP) + ")")  # window text
                # shows ! mark when help window opened
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()  # activates message box
                IpSet = True
                return IpType, IP, IpSet
        return IP

    def connect(self):
        # try to connect to a host
        global Connected, IpSet, TargetSet, UserNameSet, privateKey, publicPartner, Target
        if Connected:
            msg = QMessageBox()  # makes message box
            msg.setWindowTitle("Connect")  # Host menu title
            # Host window text
            msg.setText("You Are Already Connected To Someone")
            # shows ! mark when Host window opened
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()  # activates message box
        else:
            if UserNameSet == False:
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Username")  # menu title
                msg.setText("You Need To Add your Username ")  # window text
                # shows ! mark when window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # activates message box
            elif IpSet == False:
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Your IP")  # menu title
                msg.setText("You Need To Add your IP ")  # window text
                # shows ! mark when window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # activates message box
            elif TargetSet == False:
                msg = QMessageBox()  # makes message box
                msg.setWindowTitle("Target IP")  # menu title
                msg.setText("You Need To Add your Target IP ")  # window text
                # shows ! mark when window opened
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # activates message box
            else:
                print("Connecting To " + str(Target))
                global Client, HostUsername, fullText, connectingToHost, ipCount
                Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connecting = True
                ipCount = 0
                while connecting:
                    try:
                        Client.connect((Target, PORT))  # connect to ip on port
                        print("connected")
                        connecting = False
                        connectionError = False
                    except:
                        QtCore.QCoreApplication.processEvents()  # so gui doesnt crash
                        print("Cant Connect")
                        ipCount = ipCount + 1
                        if ipCount == 5:
                            msg = QMessageBox()  # makes message box
                            msg.setWindowTitle("Connect")  # menu title
                            msg.setText("Cant connect to " +
                                        str(Target))  # window text
                            # shows ! mark when window opened
                            msg.setIcon(QMessageBox.Critical)
                            x = msg.exec_()  # activates message box
                            connectionError = True
                            connecting = False
                        else:
                            T.sleep(2)
                if connectionError:
                    connectionError = False
                else:
                    publicPartner = rsa.PublicKey.load_pkcs1(
                        Client.recv(1024))  # receive partners encryption key
                    # send our encryption key
                    Client.send(publicKey.save_pkcs1("PEM"))

                    Client.send(rsa.encrypt(str(myUserName).encode(
                        "utf-8"), publicPartner))  # sends my username
                    HostUsername = rsa.decrypt(Client.recv(1024), privateKey).decode(
                        "utf-8")  # gets other persons username
                    fullText = str(fullText) + "\nCONNECTED WITH " + \
                        str(HostUsername)  # sets full text of the chat
                    T.sleep(1)
                    print("connected with " + str(HostUsername))
                    self.chatBox.setText(fullText)  # set text as full text
                    Connected = True
                    connectingToHost = True
                    # threads run stuff at the same time
                    t1 = threading.Thread(target=self.receiving2)
                    # threads run stuff at the same time
                    t2 = threading.Thread(target=self.sending2)
                    t1.daemon = True
                    t2.daemon = True
                    print("starting thread1")
                    t1.start()
                    print("starting thread2")
                    t2.start()
                    print("starting updateChatBox")
                    self.updateChatBox()

    def receiving2(self):
        global Client, HostUsername, sendButtonClicked, receiver, otherPersonStreaming, screenShareOn, Connected, fullText, Hosting, connectingToHost, incomingCall, notJoining, inCall, privateKey
        print("started receiving-conn")
        while True:
            try:
                if Connected == False:
                    break
                message = rsa.decrypt(Client.recv(
                    1024), privateKey).decode("utf-8")
                print("message received-conn")
                if message == "!LEAVINGTHECHAT!":
                    print(str(HostUsername) + " Has Left The Chat")
                    fullText = fullText + "\n" + \
                        str(HostUsername) + " Has Left the chat"
                    Hosting = False
                    connectingToHost = False
                    Connected = False
                    sendButtonClicked = True
                    Client.shutdown(socket.SHUT_RDWR)
                    Client.close()
                elif message == "!STARTING_SCREEN_SHARE!":
                    if screenShareOn:
                        receiver = StreamingServer(IP, 9998)
                        print("starting port 9998")
                    else:
                        receiver = StreamingServer(IP, 9999)
                        print("starting port 9999")
                    screenShareThread = threading.Thread(
                        target=receiver.start_server)
                    screenShareThread.start()
                    otherPersonStreaming = True
                elif message == "!STOP_SHARE_SCREEN!":
                    print("stoping share screen")
                    # adding to full chat
                    fullText = str(fullText) + "\nSTOPING SHARESCREEN"
                    sendButtonClicked = True  # update textbox
                    try:
                        receiver.stop_server()  # stop other person from streaming
                        otherPersonStreaming = False  # set other person streaming to false
                    except:
                        print("ERROR CANT STOP")
                elif message == "!INCOMING_CALL!":
                    incomingCall = True
                elif message == "!NOT_JOINING!":
                    notJoining = True
                elif message == "!JOINING_CALL!":
                    audioRecver1 = AudioReceiver(IP, 15567)
                    audiorecverThread1 = threading.Thread(
                        target=audioRecver1.start_server)
                    audioSend1 = AudioSender(IP, 15568)
                    audioSendThread1 = threading.Thread(
                        target=audioSend1.start_stream)

                    audiorecverThread1.start()
                    audioSendThread1.start()
                    inCall = True
                else:
                    print("\n" + str(HostUsername) + "->" +
                          str(message))  # send message to textbox
                    fullText = fullText + "\n" + \
                        str(HostUsername) + "->" + str(message)
                    print("recv2 send true")
                    sendButtonClicked = True
            except:
                pass

    def sending2(self):
        global sendButtonClicked2, fullText, Client, Connected, publicPartner
        sendButtonClicked2 = False
        print("started sending-conn")
        while True:
            if Connected == False:
                break
            if sendButtonClicked2:
                print("Sending ClientSide")
                message = str(self.textBox.text())

                Client.send(rsa.encrypt(
                    message.encode("utf-8"), publicPartner))
                fullText = fullText + "\n" + \
                    str(myUserName) + "->" + str(message)
                print("setting Text")
                sendButtonClicked2 = False
            else:
                pass


def main():
    global directory, publicIp, privateIp
    print("Public IP->" + str(publicIp))
    print("Probably Your Private IP->" + str(privateIp))
    app = QtWidgets.QApplication(sys.argv)  # starts application
    Liscord = QtWidgets.QMainWindow()  # makes main window
    fullIconDirectory = directory + "\\LiscordFlat.png"
    print(fullIconDirectory)
    Liscord.setWindowIcon(QtGui.QIcon("LiscordFlat.png")
                          )  # sets liscord app icon
    ui = Ui_Liscord()  # sets ui to Liscords ui
    ui.setupUi(Liscord)  # sets up ui
    Liscord.show()  # shows main window
    sys.exit(app.exec_())  # if exit button pressed exit


main()  # start main
