# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchwidget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLineEdit, QListView, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SearchWidget(object):
    def setupUi(self, SearchWidget):
        if not SearchWidget.objectName():
            SearchWidget.setObjectName(u"SearchWidget")
        SearchWidget.resize(638, 467)
        self.gridLayout = QGridLayout(SearchWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.listResults = QListView(SearchWidget)
        self.listResults.setObjectName(u"listResults")
        self.listResults.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout_3.addWidget(self.listResults)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineSearch = QLineEdit(SearchWidget)
        self.lineSearch.setObjectName(u"lineSearch")

        self.horizontalLayout_2.addWidget(self.lineSearch)

        self.pushSearch = QPushButton(SearchWidget)
        self.pushSearch.setObjectName(u"pushSearch")

        self.horizontalLayout_2.addWidget(self.pushSearch)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.hSpacerL = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.hSpacerL)

        self.pushSelect = QPushButton(SearchWidget)
        self.pushSelect.setObjectName(u"pushSelect")

        self.horizontalLayout_4.addWidget(self.pushSelect)

        self.hSpacerR = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.hSpacerR)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioAlbum = QRadioButton(SearchWidget)
        self.radioAlbum.setObjectName(u"radioAlbum")

        self.horizontalLayout.addWidget(self.radioAlbum)

        self.radioSong = QRadioButton(SearchWidget)
        self.radioSong.setObjectName(u"radioSong")

        self.horizontalLayout.addWidget(self.radioSong)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SearchWidget)

        QMetaObject.connectSlotsByName(SearchWidget)
    # setupUi

    def retranslateUi(self, SearchWidget):
        SearchWidget.setWindowTitle(QCoreApplication.translate("SearchWidget", u"Form", None))
        self.lineSearch.setPlaceholderText(QCoreApplication.translate("SearchWidget", u"Search for Album or Song", None))
        self.pushSearch.setText(QCoreApplication.translate("SearchWidget", u"Search", None))
        self.pushSelect.setText(QCoreApplication.translate("SearchWidget", u"Select", None))
        self.radioAlbum.setText(QCoreApplication.translate("SearchWidget", u"Album", None))
        self.radioSong.setText(QCoreApplication.translate("SearchWidget", u"Song", None))
    # retranslateUi

