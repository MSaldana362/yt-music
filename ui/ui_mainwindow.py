# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineUrl = QLineEdit(self.centralwidget)
        self.lineUrl.setObjectName(u"lineUrl")

        self.verticalLayout_2.addWidget(self.lineUrl)

        self.lineArtist = QLineEdit(self.centralwidget)
        self.lineArtist.setObjectName(u"lineArtist")

        self.verticalLayout_2.addWidget(self.lineArtist)

        self.lineAlbum = QLineEdit(self.centralwidget)
        self.lineAlbum.setObjectName(u"lineAlbum")

        self.verticalLayout_2.addWidget(self.lineAlbum)

        self.lineYear = QLineEdit(self.centralwidget)
        self.lineYear.setObjectName(u"lineYear")

        self.verticalLayout_2.addWidget(self.lineYear)

        self.lineArt = QLineEdit(self.centralwidget)
        self.lineArt.setObjectName(u"lineArt")

        self.verticalLayout_2.addWidget(self.lineArt)

        self.lineGenre = QLineEdit(self.centralwidget)
        self.lineGenre.setObjectName(u"lineGenre")

        self.verticalLayout_2.addWidget(self.lineGenre)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSpacerLeft)

        self.pushDownload = QPushButton(self.centralwidget)
        self.pushDownload.setObjectName(u"pushDownload")

        self.horizontalLayout.addWidget(self.pushDownload)

        self.hSpacerRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSpacerRight)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineUrl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Playlist or Video URL", None))
        self.lineArtist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.lineAlbum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.lineYear.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.lineArt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional) Artwork URL", None))
        self.lineGenre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional) Genre", None))
        self.pushDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

