# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/subdownloader.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.tabsMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tabsMain.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabsMain.sizePolicy().hasHeightForWidth())
        self.tabsMain.setSizePolicy(sizePolicy)
        self.tabsMain.setObjectName("tabsMain")
        self.tabSearchFile = SearchFileWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabSearchFile.sizePolicy().hasHeightForWidth())
        self.tabSearchFile.setSizePolicy(sizePolicy)
        self.tabSearchFile.setObjectName("tabSearchFile")
        self.tabsMain.addTab(self.tabSearchFile, "")
        self.tabSearchName = SearchNameWidget()
        self.tabSearchName.setObjectName("tabSearchName")
        self.tabsMain.addTab(self.tabSearchName, "")
        self.tabUpload = UploadWidget()
        self.tabUpload.setObjectName("tabUpload")
        self.tabsMain.addTab(self.tabUpload, "")
        self.vboxlayout.addWidget(self.tabsMain)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_version_description = QtWidgets.QLabel(self.frame_3)
        self.label_version_description.setObjectName("label_version_description")
        self.horizontalLayout_7.addWidget(self.label_version_description)
        self.label_version = QtWidgets.QLabel(self.frame_3)
        self.label_version.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_version.setText("X.X.XX")
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setObjectName("button_login")
        self.horizontalLayout_2.addWidget(self.button_login)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.vboxlayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.vboxlayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 714, 28))
        self.menuBar.setObjectName("menuBar")
        self.menuMain = QtWidgets.QMenu(self.menuBar)
        self.menuMain.setObjectName("menuMain")
        self.menu_Help = QtWidgets.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Preferences = QtWidgets.QMenu(self.menuBar)
        self.menu_Preferences.setObjectName("menu_Preferences")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Quit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon1)
        self.action_Quit.setObjectName("action_Quit")
        self.action_HelpHomepage = QtWidgets.QAction(MainWindow)
        self.action_HelpHomepage.setObjectName("action_HelpHomepage")
        self.action_HelpAbout = QtWidgets.QAction(MainWindow)
        self.action_HelpAbout.setObjectName("action_HelpAbout")
        self.action_HelpBug = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_HelpBug.setIcon(icon2)
        self.action_HelpBug.setObjectName("action_HelpBug")
        self.action_ShowPreferences = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ShowPreferences.setIcon(icon3)
        self.action_ShowPreferences.setObjectName("action_ShowPreferences")
        self.action_Login = QtWidgets.QAction(MainWindow)
        self.action_Login.setObjectName("action_Login")
        self.action_LogMessages = QtWidgets.QAction(MainWindow)
        self.action_LogMessages.setEnabled(False)
        self.action_LogMessages.setObjectName("action_LogMessages")
        self.action_ShowHideTreeFolder = QtWidgets.QAction(MainWindow)
        self.action_ShowHideTreeFolder.setCheckable(True)
        self.action_ShowHideTreeFolder.setChecked(True)
        self.action_ShowHideTreeFolder.setEnabled(False)
        self.action_ShowHideTreeFolder.setObjectName("action_ShowHideTreeFolder")
        self.action_LogOut = QtWidgets.QAction(MainWindow)
        self.action_LogOut.setEnabled(False)
        self.action_LogOut.setObjectName("action_LogOut")
        self.action_HelpTranslate = QtWidgets.QAction(MainWindow)
        self.action_HelpTranslate.setObjectName("action_HelpTranslate")
        self.menuMain.addAction(self.action_Login)
        self.menuMain.addAction(self.action_LogOut)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_HelpHomepage)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_HelpBug)
        self.menu_Help.addAction(self.action_HelpTranslate)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_HelpAbout)
        self.menu_Preferences.addAction(self.action_ShowPreferences)
        self.menuView.addAction(self.action_LogMessages)
        self.menuView.addAction(self.action_ShowHideTreeFolder)
        self.menuBar.addAction(self.menuMain.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menu_Preferences.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabsMain.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.tabSearchFile), _("Search from Video file(s)"))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.tabSearchName), _("Search by Movie Name"))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.tabUpload), _("Upload subtitles"))
        self.label_version_description.setText(_("version:"))
        self.button_login.setText(_("Log in"))
        self.menuMain.setTitle(_("&Main"))
        self.menu_Help.setTitle(_("&Help"))
        self.menu_Preferences.setTitle(_("&Settings"))
        self.menuView.setTitle(_("&View"))
        self.action_Quit.setText(_("Quit"))
        self.action_HelpHomepage.setText(_("Visit HomePage"))
        self.action_HelpAbout.setText(_("About..."))
        self.action_HelpAbout.setIconText(_("About"))
        self.action_HelpBug.setText(_("Report A Problem"))
        self.action_ShowPreferences.setText(_("&Configure Subdownloader..."))
        self.action_Login.setText(_("Log in..."))
        self.action_LogMessages.setText(_("Log Messages"))
        self.action_ShowHideTreeFolder.setText(_("Show/Hide Tree Folder"))
        self.action_LogOut.setText(_("Log Out"))
        self.action_HelpTranslate.setText(_("Translate This Application..."))

from subdownloader.client.gui.searchFileWidget import SearchFileWidget
from subdownloader.client.gui.searchNameWidget import SearchNameWidget
from subdownloader.client.gui.uploadWidget import UploadWidget
from subdownloader.client.gui import images_rc
