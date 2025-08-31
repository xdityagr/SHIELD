################################################################################
## Form generated from reading UI file 'newUIShieldCYAHUB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.body)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, -1, 0, 0)
        self.Heading = QFrame(self.body)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setMinimumSize(QSize(0, 80))
        self.Heading.setMaximumSize(QSize(16777215, 80))
        self.Heading.setFrameShape(QFrame.StyledPanel)
        self.Heading.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.Heading)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 10, 0, 7)
        self.Subhead = QLabel(self.Heading)
        self.Subhead.setObjectName(u"Subhead")
        font = QFont()
        font.setFamily(u"Poppins Light")
        font.setPointSize(14)
        self.Subhead.setFont(font)
        self.Subhead.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.Subhead, 1, 0, 1, 1)

        self.Title = QLabel(self.Heading)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(999, 0))
        self.Title.setMaximumSize(QSize(0, 16777215))
        font1 = QFont()
        font1.setFamily(u"Poppins ExtraBold")
        font1.setPointSize(25)
        self.Title.setFont(font1)
        self.Title.setStyleSheet(u"color: rgb(38, 172, 255);")

        self.gridLayout_3.addWidget(self.Title, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.Heading)

        self.TabFrame = QFrame(self.body)
        self.TabFrame.setObjectName(u"TabFrame")
        self.TabFrame.setFrameShape(QFrame.StyledPanel)
        self.TabFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.TabFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.TabFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"/* Tab Bar */\n"
"QTabBar {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: #333;                 /* Text color of the tab bar */\n"
"    padding: 5px 10px;           /* Padding around each tab */\n"
"    border: none;    \n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"/* Selected Tab */\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(38, 172, 255);   /* Background color of the selected tab */\n"
"    color: #fff;     \n"
"border:nonel;\n"
"	border-radius:0px;\n"
"	border-top-left-radius:8px;\n"
"	border-top-right-radius:8px;         /* Text color of the selected tab */\n"
"}\n"
"\n"
"/* Unselected Tabs */\n"
"QTabBar::tab {\n"
"    background-color: none;      /* Background color of unselected tabs */\n"
"    color: #555;             \n"
"	border-radius:0px;\n"
"	padding:8px;\n"
"	padding-left:10px;    /* Text color of unselected tabs */\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"/* Tab Contents */\n"
"QTabWidget::pane { \n"
"border-top: 1px solid rgb(38, 172, 255);    /* Border arou"
                        "nd the tab contents */\n"
"    background-color: #f9f9f9;   /* Background color of the tab contents */\n"
"    color: #333;        \n"
"\n"
"}\n"
"")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.label_6 = QLabel(self.homeTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 40, 351, 191))
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Poppins Medium")
        font2.setPointSize(22)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid black;\n"
"border-radius:8px;")
        self.label_6.setWordWrap(True)
        self.frame_4 = QFrame(self.homeTab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 240, 351, 221))
        self.frame_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid black;\n"
"border-radius:8px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 131, 61))
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Poppins ExtraBold")
        font3.setPointSize(34)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"border:none;\n"
"color:rgb(255, 57, 57);")
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 80, 121, 61))
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"border:none;\n"
"color: rgb(112, 255, 110);")
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 150, 331, 61))
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"border:none;\n"
"color: rgb(38, 172, 255);")
        self.label_9.setWordWrap(True)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 20, 101, 41))
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamily(u"Poppins Light")
        font4.setPointSize(12)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"border:none;")
        self.label_10.setWordWrap(True)
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 90, 101, 41))
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(16777215, 16777215))
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"border:none;")
        self.label_11.setWordWrap(True)
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(140, 160, 101, 41))
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"border:none;")
        self.label_12.setWordWrap(True)
        self.frame_5 = QFrame(self.homeTab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(390, 40, 391, 421))
        self.frame_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid black;\n"
"border-radius:8px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 311, 41))
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Poppins SemiBold")
        font5.setPointSize(17)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);border:none")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 50, 201, 31))
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamily(u"Poppins Medium")
        font6.setPointSize(14)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"color: rgb(112, 255, 110);\n"
"background:none;\n"
"border:none")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 351, 331))
        self.label_3.setStyleSheet(u"border:none")
        self.label_3.setPixmap(QPixmap(u"Images/indiamap.png"))
        self.label_3.setScaledContents(True)
        self.tabWidget.addTab(self.homeTab, "")
        self.missingTab = QWidget()
        self.missingTab.setObjectName(u"missingTab")
        self.textEdit_3 = QTextEdit(self.missingTab)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(20, 170, 261, 31))
        font7 = QFont()
        font7.setPointSize(10)
        self.textEdit_3.setFont(font7)
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit = QTextEdit(self.missingTab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 90, 261, 31))
        self.textEdit.setFont(font7)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2 = QTextEdit(self.missingTab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(20, 240, 261, 31))
        self.textEdit_2.setFont(font7)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_13 = QLabel(self.missingTab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 210, 251, 21))
        font8 = QFont()
        font8.setFamily(u"Poppins SemiBold")
        font8.setPointSize(10)
        self.label_13.setFont(font8)
        self.label_14 = QLabel(self.missingTab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 68, 171, 21))
        self.label_14.setFont(font8)
        self.label_15 = QLabel(self.missingTab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 140, 231, 21))
        self.label_15.setFont(font8)
        self.startSearch = QPushButton(self.missingTab)
        self.startSearch.setObjectName(u"startSearch")
        self.startSearch.setGeometry(QRect(480, 400, 301, 61))
        font9 = QFont()
        font9.setFamily(u"Poppins Medium")
        font9.setPointSize(12)
        self.startSearch.setFont(font9)
        self.startSearch.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 172, 255);\n"
"	border-radius:8px;\n"
"color:white;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(92, 198, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(33, 152, 221);\n"
"}")
        self.label_17 = QLabel(self.missingTab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(310, 90, 141, 161))
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_17.setPixmap(QPixmap(u"Images/usericon.png"))
        self.label_17.setScaledContents(True)
        self.label_18 = QLabel(self.missingTab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 290, 231, 21))
        self.label_18.setFont(font8)
        self.textEdit_4 = QTextEdit(self.missingTab)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(20, 320, 261, 61))
        self.textEdit_4.setFont(font7)
        self.textEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5 = QTextEdit(self.missingTab)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(20, 420, 261, 51))
        self.textEdit_5.setFont(font7)
        self.textEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_19 = QLabel(self.missingTab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 390, 231, 21))
        self.label_19.setFont(font8)
        self.addPhoto = QPushButton(self.missingTab)
        self.addPhoto.setObjectName(u"addPhoto")
        self.addPhoto.setGeometry(QRect(310, 250, 142, 41))
        font10 = QFont()
        font10.setFamily(u"Poppins")
        font10.setPointSize(10)
        self.addPhoto.setFont(font10)
        self.addPhoto.setStyleSheet(u"QPushButton {\n"
"border-left: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;\n"
"background-color: white;\n"
"}\n"
"QPushButton::hover {\n"
"border-left: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;\n"
"	background-color: rgb(201, 242, 255);\n"
"}\n"
"")
        self.addPhoto.setAutoDefault(False)
        self.addPhoto.setFlat(True)
        self.label_16 = QLabel(self.missingTab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 20, 431, 31))
        self.label_16.setMinimumSize(QSize(150, 0))
        self.label_16.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setFamily(u"Poppins SemiBold")
        font11.setPointSize(21)
        self.label_16.setFont(font11)
        self.label_16.setStyleSheet(u"color: rgb(38, 172, 255);")
        self.tabWidget.addTab(self.missingTab, "")
        self.scanningTab = QWidget()
        self.scanningTab.setObjectName(u"scanningTab")
        self.layoutWidget = QWidget(self.scanningTab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 774, 263))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.originalIrisLabel = QLabel(self.layoutWidget)
        self.originalIrisLabel.setObjectName(u"originalIrisLabel")
        font12 = QFont()
        font12.setFamily(u"Poppins Medium")
        font12.setPointSize(10)
        self.originalIrisLabel.setFont(font12)

        self.horizontalLayout_4.addWidget(self.originalIrisLabel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.origIrisImageViewer = QFrame(self.layoutWidget)
        self.origIrisImageViewer.setObjectName(u"origIrisImageViewer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.origIrisImageViewer.sizePolicy().hasHeightForWidth())
        self.origIrisImageViewer.setSizePolicy(sizePolicy)
        self.origIrisImageViewer.setMinimumSize(QSize(300, 200))
        self.origIrisImageViewer.setStyleSheet(u"border: 2px dashed #434343;")
        self.gridLayout_4 = QGridLayout(self.origIrisImageViewer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.irisImageO = QLabel(self.origIrisImageViewer)
        self.irisImageO.setObjectName(u"irisImageO")
        self.irisImageO.setStyleSheet(u"border:none;")
        self.irisImageO.setScaledContents(True)

        self.gridLayout_4.addWidget(self.irisImageO, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.origIrisImageViewer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.loadOriginalIris = QPushButton(self.layoutWidget)
        self.loadOriginalIris.setObjectName(u"loadOriginalIris")
        self.loadOriginalIris.setMinimumSize(QSize(0, 0))
        self.loadOriginalIris.setMaximumSize(QSize(50, 16777215))
        self.loadOriginalIris.setFont(font7)
        self.loadOriginalIris.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 172, 255);\n"
"	border-radius:4px;\n"
"color:white;\n"
"width:80px;\n"
"height:20px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(92, 198, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(33, 152, 221);\n"
"}")

        self.horizontalLayout_5.addWidget(self.loadOriginalIris)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)

        self.queryIrisLabel = QLabel(self.layoutWidget)
        self.queryIrisLabel.setObjectName(u"queryIrisLabel")
        self.queryIrisLabel.setFont(font12)

        self.horizontalLayout_7.addWidget(self.queryIrisLabel)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_15)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.queryIrisImageViewer = QFrame(self.layoutWidget)
        self.queryIrisImageViewer.setObjectName(u"queryIrisImageViewer")
        self.queryIrisImageViewer.setMinimumSize(QSize(300, 200))
        self.queryIrisImageViewer.setStyleSheet(u"border: 2px dashed rgb(67, 67, 67);")
        self.gridLayout_5 = QGridLayout(self.queryIrisImageViewer)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.IrisImageQ = QLabel(self.queryIrisImageViewer)
        self.IrisImageQ.setObjectName(u"IrisImageQ")
        self.IrisImageQ.setStyleSheet(u"border:none;")
        self.IrisImageQ.setScaledContents(True)

        self.gridLayout_5.addWidget(self.IrisImageQ, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.queryIrisImageViewer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.loadQueryIris = QPushButton(self.layoutWidget)
        self.loadQueryIris.setObjectName(u"loadQueryIris")
        self.loadQueryIris.setMaximumSize(QSize(50, 16777215))
        self.loadQueryIris.setFont(font7)
        self.loadQueryIris.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 172, 255);\n"
"	border-radius:4px;\n"
"color:white;\n"
"width:80px;\n"
"height:20px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(92, 198, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(33, 152, 221);\n"
"}")

        self.horizontalLayout_8.addWidget(self.loadQueryIris)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.line = QFrame(self.scanningTab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-20, 300, 791, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.match_found_frame = QFrame(self.scanningTab)
        self.match_found_frame.setObjectName(u"match_found_frame")
        self.match_found_frame.setGeometry(QRect(0, 339, 821, 141))
        self.match_found_frame.setStyleSheet(u"background-color: rgb(212, 240, 255);")
        self.match_found_frame.setFrameShape(QFrame.StyledPanel)
        self.match_found_frame.setFrameShadow(QFrame.Raised)
        self.matchFound = QLabel(self.match_found_frame)
        self.matchFound.setObjectName(u"matchFound")
        self.matchFound.setGeometry(QRect(230, 10, 351, 121))
        self.matchFound.setMinimumSize(QSize(700, 0))
        self.matchFound.setMaximumSize(QSize(16777215, 16777215))
        self.matchFound.setFont(font1)
        self.matchFound.setStyleSheet(u"color: rgb(38, 172, 255);")
        self.goButton = QPushButton(self.scanningTab)
        self.goButton.setObjectName(u"goButton")
        self.goButton.setGeometry(QRect(320, 280, 120, 50))
        font13 = QFont()
        font13.setFamily(u"Poppins SemiBold")
        font13.setPointSize(18)
        self.goButton.setFont(font13)
        self.goButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(38, 172, 255);\n"
"	border-radius:4px;\n"
"color:white;\n"
"width:120px;\n"
"height:50px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(92, 198, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(33, 152, 221);\n"
"}")
        self.frame_8 = QFrame(self.scanningTab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(650, 300, 171, 21))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.matchThresholdSpinBox = QDoubleSpinBox(self.frame_8)
        self.matchThresholdSpinBox.setObjectName(u"matchThresholdSpinBox")
        self.matchThresholdSpinBox.setGeometry(QRect(118, 0, 49, 20))
        self.matchThresholdSpinBox.setSingleStep(0.010000000000000)
        self.matchThresholdSpinBox.setValue(0.000000000000000)
        self.matchThresholdLabel = QLabel(self.frame_8)
        self.matchThresholdLabel.setObjectName(u"matchThresholdLabel")
        self.matchThresholdLabel.setGeometry(QRect(0, 0, 121, 20))
        font14 = QFont()
        font14.setFamily(u"Poppins Medium")
        self.matchThresholdLabel.setFont(font14)
        self.matchThresholdLabel.raise_()
        self.matchThresholdSpinBox.raise_()
        self.tabWidget.addTab(self.scanningTab, "")
        self.line.raise_()
        self.match_found_frame.raise_()
        self.layoutWidget.raise_()
        self.goButton.raise_()
        self.frame_8.raise_()
        self.statusTab = QWidget()
        self.statusTab.setObjectName(u"statusTab")
        self.statusFrame = QFrame(self.statusTab)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setGeometry(QRect(29, 19, 771, 281))
        self.statusFrame.setStyleSheet(u"border-radius:8px;")
        self.statusFrame.setFrameShape(QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Raised)
        self.found_content = QLabel(self.statusFrame)
        self.found_content.setObjectName(u"found_content")
        self.found_content.setGeometry(QRect(20, 100, 691, 141))
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        self.found_content.setFont(font15)
        self.found_content.setStyleSheet(u" background-color:none;color:black;")
        self.found_content.setWordWrap(True)
        self.line_2 = QLabel(self.statusFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 70, 770, 1))
        self.line_2.setStyleSheet(u"background-color: rgb(44, 44, 44);")

        self.found = QLabel(self.statusFrame)
        self.found.setObjectName(u"found")
        self.found.setGeometry(QRect(20, 20, 431, 41))
        self.found.setMinimumSize(QSize(150, 0))
        self.found.setMaximumSize(QSize(16777215, 16777215))
        self.found.setFont(font11)
        self.found.setStyleSheet(u"color: rgb(38, 172, 255);")

        self.tabWidget.addTab(self.statusTab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.TabFrame)


        self.gridLayout.addWidget(self.body, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.addPhoto.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("SHIELD WSN Cluster Head Console", u"SHIELD WSN Cluster Head Console", None))
        self.Subhead.setText(QCoreApplication.translate("MainWindow", u"Cluster-head Console", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"S.H.I.E.L.D", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#26acff;\">Breaking Barriers:</span></p><p><span style=\" font-size:14pt;\">Transforming the Fight Against Human Trafficking with Unmatched Innovation!</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2400", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"3600", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lives Lost.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Lives Saved.", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Searching ...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Wireless Sensor Network", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.label_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Missing Person's Aadhar Number", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Missing Person's Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Missing Person's Phone Number", None))
        self.startSearch.setText(QCoreApplication.translate("MainWindow", u"Start NationWide Search", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Last seen location", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Physical Attributes", None))
        self.addPhoto.setText(QCoreApplication.translate("MainWindow", u"Add Photograph", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Report a missing person:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.missingTab), QCoreApplication.translate("MainWindow", u"Report a missing person", None))
        self.originalIrisLabel.setText(QCoreApplication.translate("MainWindow", u"Original Iris - Untitled", None))
        self.irisImageO.setText("")
        self.loadOriginalIris.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.queryIrisLabel.setText(QCoreApplication.translate("MainWindow", u"Query Iris - Untitled", None))
        self.IrisImageQ.setText("")
        self.loadQueryIris.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.matchFound.setText(QCoreApplication.translate("MainWindow", u"MATCH FOUND, 38%", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.matchThresholdLabel.setText(QCoreApplication.translate("MainWindow", u"Accuracy Threshold :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scanningTab), QCoreApplication.translate("MainWindow", u"Iris Scanning", None))
        self.found.setText(QCoreApplication.translate("MainWindow", u"Found Missing Person : Aditya", None))
        self.line_2.setText("")
        self.found_content.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aadhaar :</span><span style=\" font-size:10pt;\"> 2015XXXXXX</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Phone Number :</span><span style=\" font-size:10pt;\"> 9899XXXXX</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Last Located at :</span><span style=\" font-size:10pt;\"> New Delhi, Rohini, Main Road [3:15 PM]</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Via</span><span style=\" font-size:10pt;\"> : Facial Recoginiton (WSN)<br/></span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statusTab), QCoreApplication.translate("MainWindow", u"Status", None))
    # retranslateUi

