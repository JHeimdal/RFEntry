# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/bet_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Betalat(object):
    def setupUi(self, Betalat):
        Betalat.setObjectName("Betalat")
        Betalat.resize(315, 115)
        self.verticalLayout = QtWidgets.QVBoxLayout(Betalat)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Betalat)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_ja = QtWidgets.QPushButton(Betalat)
        self.button_ja.setObjectName("button_ja")
        self.horizontalLayout.addWidget(self.button_ja)
        self.button_nej = QtWidgets.QPushButton(Betalat)
        self.button_nej.setObjectName("button_nej")
        self.horizontalLayout.addWidget(self.button_nej)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Betalat)
        QtCore.QMetaObject.connectSlotsByName(Betalat)

    def retranslateUi(self, Betalat):
        _translate = QtCore.QCoreApplication.translate
        Betalat.setWindowTitle(_translate("Betalat", "Betalat?"))
        self.label.setText(_translate("Betalat", "Har medlemen betalat?"))
        self.button_ja.setText(_translate("Betalat", "Ja"))
        self.button_nej.setText(_translate("Betalat", "Nej"))
