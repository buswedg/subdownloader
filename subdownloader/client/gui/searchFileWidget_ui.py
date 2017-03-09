# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchFileWidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchFileWidget(object):
    def setupUi(self, SearchFileWidget):
        SearchFileWidget.setObjectName("SearchFileWidget")
        SearchFileWidget.resize(795, 518)
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchFileWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(SearchFileWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem = QtWidgets.QSpacerItem(88, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(88, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.buttonSearchSelectVideos = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearchSelectVideos.sizePolicy().hasHeightForWidth())
        self.buttonSearchSelectVideos.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/open_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSearchSelectVideos.setIcon(icon)
        self.buttonSearchSelectVideos.setIconSize(QtCore.QSize(16, 16))
        self.buttonSearchSelectVideos.setObjectName("buttonSearchSelectVideos")
        self.horizontalLayout_6.addWidget(self.buttonSearchSelectVideos)
        self.buttonSearchSelectFolder = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearchSelectFolder.sizePolicy().hasHeightForWidth())
        self.buttonSearchSelectFolder.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSearchSelectFolder.setIcon(icon1)
        self.buttonSearchSelectFolder.setIconSize(QtCore.QSize(16, 16))
        self.buttonSearchSelectFolder.setObjectName("buttonSearchSelectFolder")
        self.horizontalLayout_6.addWidget(self.buttonSearchSelectFolder)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.folderView = QtWidgets.QTreeView(self.frame_2)
        self.folderView.setObjectName("folderView")
        self.verticalLayout_3.addWidget(self.folderView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonRefresh = QtWidgets.QPushButton(self.frame_2)
        self.buttonRefresh.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonRefresh.setFont(font)
        self.buttonRefresh.setCheckable(False)
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.horizontalLayout_4.addWidget(self.buttonRefresh)
        self.buttonFind = QtWidgets.QPushButton(self.frame_2)
        self.buttonFind.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonFind.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonFind.setIcon(icon2)
        self.buttonFind.setIconSize(QtCore.QSize(16, 16))
        self.buttonFind.setObjectName("buttonFind")
        self.horizontalLayout_4.addWidget(self.buttonFind)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.groupBox_videosFound = QtWidgets.QFrame(self.splitter)
        self.groupBox_videosFound.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.groupBox_videosFound.setFrameShadow(QtWidgets.QFrame.Raised)
        self.groupBox_videosFound.setObjectName("groupBox_videosFound")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_videosFound)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedSearchResult = QtWidgets.QStackedWidget(self.groupBox_videosFound)
        self.stackedSearchResult.setObjectName("stackedSearchResult")
        self.pageIntroduction = QtWidgets.QWidget()
        self.pageIntroduction.setObjectName("pageIntroduction")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.pageIntroduction)
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.introductionHelp = QtWidgets.QTextBrowser(self.pageIntroduction)
        self.introductionHelp.setObjectName("introductionHelp")
        self.verticalLayout_11.addWidget(self.introductionHelp)
        self.stackedSearchResult.addWidget(self.pageIntroduction)
        self.pageSearchResult = QtWidgets.QWidget()
        self.pageSearchResult.setObjectName("pageSearchResult")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.pageSearchResult)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.layoutTopVideos = QtWidgets.QHBoxLayout()
        self.layoutTopVideos.setObjectName("layoutTopVideos")
        self.label_videosFound = QtWidgets.QLabel(self.pageSearchResult)
        self.label_videosFound.setObjectName("label_videosFound")
        self.layoutTopVideos.addWidget(self.label_videosFound)
        spacerItem2 = QtWidgets.QSpacerItem(88, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutTopVideos.addItem(spacerItem2)
        self.label_filterBy = QtWidgets.QLabel(self.pageSearchResult)
        self.label_filterBy.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_filterBy.setFont(font)
        self.label_filterBy.setObjectName("label_filterBy")
        self.layoutTopVideos.addWidget(self.label_filterBy)
        self.filterLanguageForVideo = LanguageComboBox(self.pageSearchResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLanguageForVideo.sizePolicy().hasHeightForWidth())
        self.filterLanguageForVideo.setSizePolicy(sizePolicy)
        self.filterLanguageForVideo.setMinimumSize(QtCore.QSize(100, 0))
        self.filterLanguageForVideo.setObjectName("filterLanguageForVideo")
        self.layoutTopVideos.addWidget(self.filterLanguageForVideo)
        self.layoutTopVideos.setStretch(3, 1)
        self.verticalLayout_12.addLayout(self.layoutTopVideos)
        self.videoView = QtWidgets.QTreeView(self.pageSearchResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoView.sizePolicy().hasHeightForWidth())
        self.videoView.setSizePolicy(sizePolicy)
        self.videoView.setObjectName("videoView")
        self.verticalLayout_12.addWidget(self.videoView)
        self.layoutBottomVideos = QtWidgets.QHBoxLayout()
        self.layoutBottomVideos.setContentsMargins(-1, -1, -1, 0)
        self.layoutBottomVideos.setObjectName("layoutBottomVideos")
        self.buttonIMDB = QtWidgets.QPushButton(self.pageSearchResult)
        self.buttonIMDB.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIMDB.setIcon(icon3)
        self.buttonIMDB.setIconSize(QtCore.QSize(32, 16))
        self.buttonIMDB.setObjectName("buttonIMDB")
        self.layoutBottomVideos.addWidget(self.buttonIMDB)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutBottomVideos.addItem(spacerItem3)
        self.buttonPlay = QtWidgets.QPushButton(self.pageSearchResult)
        self.buttonPlay.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(icon4)
        self.buttonPlay.setObjectName("buttonPlay")
        self.layoutBottomVideos.addWidget(self.buttonPlay)
        self.buttonDownload = QtWidgets.QPushButton(self.pageSearchResult)
        self.buttonDownload.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonDownload.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDownload.setIcon(icon5)
        self.buttonDownload.setObjectName("buttonDownload")
        self.layoutBottomVideos.addWidget(self.buttonDownload)
        self.verticalLayout_12.addLayout(self.layoutBottomVideos)
        self.stackedSearchResult.addWidget(self.pageSearchResult)
        self.verticalLayout_8.addWidget(self.stackedSearchResult)
        self.verticalLayout_6.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(SearchFileWidget)
        self.stackedSearchResult.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SearchFileWidget)

    def retranslateUi(self, SearchFileWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label_11.setText(_("Select the video/folder that needs subtitles:"))
        self.buttonSearchSelectVideos.setToolTip(_("Select videos that need subtitles"))
        self.buttonSearchSelectVideos.setText(_("Select videos..."))
        self.buttonSearchSelectFolder.setToolTip(_("Click here to Search the subtitles of the movies in that folder"))
        self.buttonSearchSelectFolder.setText(_("Select folder..."))
        self.buttonRefresh.setText(_("Refresh list"))
        self.buttonFind.setToolTip(_("Click here to Search the subtitles of the movies in that folder"))
        self.buttonFind.setText(_("Search subtitles"))
        self.label_videosFound.setText(_("Videos/Subtitles found:"))
        self.label_filterBy.setText(_("Filter by:"))
        self.buttonIMDB.setText(_("Movie Info"))
        self.buttonPlay.setText(_("Play"))
        self.buttonDownload.setText(_("Download"))

from subdownloader.client.gui.languageComboBox import LanguageComboBox
from subdownloader.client.gui import images_rc
