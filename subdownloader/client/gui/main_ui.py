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
        self.tabUpload = QtWidgets.QWidget()
        self.tabUpload.setObjectName("tabUpload")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.tabUpload)
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setSpacing(1)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabUpload)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(-1, 1, -1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buttonUploadBrowseFolder = QtWidgets.QToolButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/openfolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadBrowseFolder.setIcon(icon1)
        self.buttonUploadBrowseFolder.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadBrowseFolder.setObjectName("buttonUploadBrowseFolder")
        self.horizontalLayout_5.addWidget(self.buttonUploadBrowseFolder)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.buttonUploadPlusRow = QtWidgets.QToolButton(self.groupBox_2)
        self.buttonUploadPlusRow.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadPlusRow.setIcon(icon2)
        self.buttonUploadPlusRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadPlusRow.setObjectName("buttonUploadPlusRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadPlusRow)
        self.buttonUploadMinusRow = QtWidgets.QToolButton(self.groupBox_2)
        self.buttonUploadMinusRow.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadMinusRow.setIcon(icon3)
        self.buttonUploadMinusRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadMinusRow.setObjectName("buttonUploadMinusRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadMinusRow)
        self.buttonUploadDeleteAllRow = QtWidgets.QToolButton(self.groupBox_2)
        self.buttonUploadDeleteAllRow.setEnabled(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/delete_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadDeleteAllRow.setIcon(icon4)
        self.buttonUploadDeleteAllRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadDeleteAllRow.setObjectName("buttonUploadDeleteAllRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadDeleteAllRow)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.buttonUploadUpRow = QtWidgets.QToolButton(self.groupBox_2)
        self.buttonUploadUpRow.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadUpRow.setIcon(icon5)
        self.buttonUploadUpRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadUpRow.setObjectName("buttonUploadUpRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadUpRow)
        self.buttonUploadDownRow = QtWidgets.QToolButton(self.groupBox_2)
        self.buttonUploadDownRow.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadDownRow.setIcon(icon6)
        self.buttonUploadDownRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadDownRow.setObjectName("buttonUploadDownRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadDownRow)
        spacerItem = QtWidgets.QSpacerItem(401, 33, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.uploadView = UploadListView(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadView.sizePolicy().hasHeightForWidth())
        self.uploadView.setSizePolicy(sizePolicy)
        self.uploadView.setMinimumSize(QtCore.QSize(0, 0))
        self.uploadView.setBaseSize(QtCore.QSize(0, 0))
        self.uploadView.setAcceptDrops(True)
        self.uploadView.setAutoScrollMargin(16)
        self.uploadView.setDragEnabled(True)
        self.uploadView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.uploadView.setAlternatingRowColors(True)
        self.uploadView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.uploadView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.uploadView.setGridStyle(QtCore.Qt.DotLine)
        self.uploadView.setObjectName("uploadView")
        self.verticalLayout.addWidget(self.uploadView)
        self.vboxlayout2.addWidget(self.groupBox_2)
        self.uploadDetailsGroupBox = QtWidgets.QGroupBox(self.tabUpload)
        self.uploadDetailsGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.uploadDetailsGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.uploadDetailsGroupBox.setObjectName("uploadDetailsGroupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.uploadDetailsGroupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.uploadIMDB = QtWidgets.QComboBox(self.uploadDetailsGroupBox)
        self.uploadIMDB.setObjectName("uploadIMDB")
        self.uploadIMDB.addItem("")
        self.gridLayout.addWidget(self.uploadIMDB, 1, 2, 1, 1)
        self.buttonUploadFindIMDB = QtWidgets.QPushButton(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonUploadFindIMDB.sizePolicy().hasHeightForWidth())
        self.buttonUploadFindIMDB.setSizePolicy(sizePolicy)
        self.buttonUploadFindIMDB.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonUploadFindIMDB.setMaximumSize(QtCore.QSize(120, 16777215))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadFindIMDB.setIcon(icon7)
        self.buttonUploadFindIMDB.setObjectName("buttonUploadFindIMDB")
        self.gridLayout.addWidget(self.buttonUploadFindIMDB, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_autodetect_imdb = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        self.label_autodetect_imdb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_autodetect_imdb.sizePolicy().hasHeightForWidth())
        self.label_autodetect_imdb.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_autodetect_imdb.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_autodetect_imdb.setFont(font)
        self.label_autodetect_imdb.setLineWidth(0)
        self.label_autodetect_imdb.setTextFormat(QtCore.Qt.PlainText)
        self.label_autodetect_imdb.setScaledContents(False)
        self.label_autodetect_imdb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_autodetect_imdb.setObjectName("label_autodetect_imdb")
        self.gridLayout.addWidget(self.label_autodetect_imdb, 0, 2, 1, 1)
        self.label_autodetect_lang = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_autodetect_lang.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_autodetect_lang.setFont(font)
        self.label_autodetect_lang.setTextFormat(QtCore.Qt.PlainText)
        self.label_autodetect_lang.setObjectName("label_autodetect_lang")
        self.gridLayout.addWidget(self.label_autodetect_lang, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.uploadReleaseText = QtWidgets.QLineEdit(self.uploadDetailsGroupBox)
        self.uploadReleaseText.setObjectName("uploadReleaseText")
        self.gridLayout.addWidget(self.uploadReleaseText, 4, 2, 1, 1)
        self.uploadComments = QtWidgets.QTextEdit(self.uploadDetailsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadComments.sizePolicy().hasHeightForWidth())
        self.uploadComments.setSizePolicy(sizePolicy)
        self.uploadComments.setMaximumSize(QtCore.QSize(16777215, 50))
        self.uploadComments.setObjectName("uploadComments")
        self.gridLayout.addWidget(self.uploadComments, 5, 2, 1, 1)
        self.buttonUpload = QtWidgets.QPushButton(self.uploadDetailsGroupBox)
        self.buttonUpload.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonUpload.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUpload.setIcon(icon8)
        self.buttonUpload.setIconSize(QtCore.QSize(24, 24))
        self.buttonUpload.setObjectName("buttonUpload")
        self.gridLayout.addWidget(self.buttonUpload, 5, 3, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.uploadLanguages = QtWidgets.QComboBox(self.uploadDetailsGroupBox)
        self.uploadLanguages.setObjectName("uploadLanguages")
        self.horizontalLayout_12.addWidget(self.uploadLanguages)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.vboxlayout2.addWidget(self.uploadDetailsGroupBox)
        self.vboxlayout1.addLayout(self.vboxlayout2)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon9)
        self.action_Quit.setObjectName("action_Quit")
        self.action_HelpHomepage = QtWidgets.QAction(MainWindow)
        self.action_HelpHomepage.setObjectName("action_HelpHomepage")
        self.action_HelpAbout = QtWidgets.QAction(MainWindow)
        self.action_HelpAbout.setObjectName("action_HelpAbout")
        self.action_HelpBug = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_HelpBug.setIcon(icon10)
        self.action_HelpBug.setObjectName("action_HelpBug")
        self.action_ShowPreferences = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ShowPreferences.setIcon(icon11)
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
        self.tabsMain.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.tabSearchFile), _("Search from Video file(s)"))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.tabSearchName), _("Search by Movie Name"))
        self.groupBox_2.setTitle(_("Select the videos and subtitles  (only subtitles will be uploaded):"))
        self.buttonUploadBrowseFolder.setText(_("..."))
        self.buttonUploadPlusRow.setText(_("..."))
        self.buttonUploadMinusRow.setText(_("..."))
        self.buttonUploadDeleteAllRow.setToolTip(_("Empty the list"))
        self.buttonUploadDeleteAllRow.setText(_("..."))
        self.buttonUploadUpRow.setText(_("..."))
        self.buttonUploadDownRow.setText(_("..."))
        self.uploadDetailsGroupBox.setTitle(_("Details:"))
        self.label_4.setText(_translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">*</span></p></body></html>"))
        self.label.setText(_("Movie Title:"))
        self.uploadIMDB.setItemText(0, _("Click on the Find button to identify the movie"))
        self.buttonUploadFindIMDB.setText(_("Find"))
        self.label_8.setText(_translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">*</span></p></body></html>"))
        self.label_autodetect_imdb.setText(_("..."))
        self.label_autodetect_lang.setText(_("..."))
        self.label_6.setText(_("Release name:"))
        self.label_7.setText(_("Comments:"))
        self.label_5.setText(_("Subtitle Language:"))
        self.buttonUpload.setText(_("Upload"))
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
from subdownloader.client.gui.uploadlistview import UploadListView
from subdownloader.client.gui import images_rc
