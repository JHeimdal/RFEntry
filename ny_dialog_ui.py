# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ny_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NyMedlem(object):
    def setupUi(self, NyMedlem):
        NyMedlem.setObjectName("NyMedlem")
        NyMedlem.resize(658, 778)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NyMedlem)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ID_lb = QtWidgets.QLabel(NyMedlem)
        self.ID_lb.setObjectName("ID_lb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ID_lb)
        self.ID_val = QtWidgets.QLabel(NyMedlem)
        self.ID_val.setObjectName("ID_val")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID_val)
        self.namn_id = QtWidgets.QLabel(NyMedlem)
        self.namn_id.setObjectName("namn_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.namn_id)
        self.namn = QtWidgets.QLineEdit(NyMedlem)
        self.namn.setObjectName("namn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.namn)
        self.pers_num_lb = QtWidgets.QLabel(NyMedlem)
        self.pers_num_lb.setObjectName("pers_num_lb")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pers_num_lb)
        self.pers_num = QtWidgets.QLineEdit(NyMedlem)
        self.pers_num.setPlaceholderText("")
        self.pers_num.setObjectName("pers_num")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pers_num)
        self.kon_lb = QtWidgets.QLabel(NyMedlem)
        self.kon_lb.setObjectName("kon_lb")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.kon_lb)
        self.kon = QtWidgets.QComboBox(NyMedlem)
        self.kon.setObjectName("kon")
        self.kon.addItem("")
        self.kon.addItem("")
        self.kon.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.kon)
        self.email_lb = QtWidgets.QLabel(NyMedlem)
        self.email_lb.setObjectName("email_lb")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.email_lb)
        self.email = QtWidgets.QLineEdit(NyMedlem)
        self.email.setObjectName("email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.email)
        self.adress_lb = QtWidgets.QLabel(NyMedlem)
        self.adress_lb.setObjectName("adress_lb")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.adress_lb)
        self.adress = QtWidgets.QLineEdit(NyMedlem)
        self.adress.setObjectName("adress")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.adress)
        self.postnum_lb = QtWidgets.QLabel(NyMedlem)
        self.postnum_lb.setObjectName("postnum_lb")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.postnum_lb)
        self.post_num = QtWidgets.QLineEdit(NyMedlem)
        self.post_num.setAutoFillBackground(False)
        self.post_num.setObjectName("post_num")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.post_num)
        self.ort_lb = QtWidgets.QLabel(NyMedlem)
        self.ort_lb.setObjectName("ort_lb")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.ort_lb)
        self.ort = QtWidgets.QLineEdit(NyMedlem)
        self.ort.setObjectName("ort")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.ort)
        self.grupp_lb = QtWidgets.QLabel(NyMedlem)
        self.grupp_lb.setObjectName("grupp_lb")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.grupp_lb)
        self.group = QtWidgets.QComboBox(NyMedlem)
        self.group.setCurrentText("")
        self.group.setObjectName("group")
        self.group.addItem("")
        self.group.addItem("")
        self.group.addItem("")
        self.group.addItem("")
        self.group.addItem("")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.group)
        self.Betalt_lb = QtWidgets.QLabel(NyMedlem)
        self.Betalt_lb.setObjectName("Betalt_lb")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Betalt_lb)
        self.betalt = QtWidgets.QRadioButton(NyMedlem)
        self.betalt.setObjectName("betalt")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.betalt)
        self.kommentar_lb = QtWidgets.QLabel(NyMedlem)
        self.kommentar_lb.setObjectName("kommentar_lb")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.kommentar_lb)
        self.kommentar = QtWidgets.QTextEdit(NyMedlem)
        self.kommentar.setObjectName("kommentar")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.kommentar)
        self.telefon_lb = QtWidgets.QLabel(NyMedlem)
        self.telefon_lb.setObjectName("telefon_lb")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.telefon_lb)
        self.telefon = QtWidgets.QLineEdit(NyMedlem)
        self.telefon.setObjectName("telefon")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.telefon)
        self.verticalLayout.addLayout(self.formLayout)
        self.malsman = QtWidgets.QGroupBox(NyMedlem)
        self.malsman.setEnabled(False)
        self.malsman.setFlat(True)
        self.malsman.setCheckable(False)
        self.malsman.setObjectName("malsman")
        self.formLayout_3 = QtWidgets.QFormLayout(self.malsman)
        self.formLayout_3.setObjectName("formLayout_3")
        self.namnlb_mm = QtWidgets.QLabel(self.malsman)
        self.namnlb_mm.setObjectName("namnlb_mm")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.namnlb_mm)
        self.namn_mm = QtWidgets.QLineEdit(self.malsman)
        self.namn_mm.setObjectName("namn_mm")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.namn_mm)
        self.emaillb_mm = QtWidgets.QLabel(self.malsman)
        self.emaillb_mm.setObjectName("emaillb_mm")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.emaillb_mm)
        self.email_mm = QtWidgets.QLineEdit(self.malsman)
        self.email_mm.setObjectName("email_mm")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.email_mm)
        self.telefonlb_mm = QtWidgets.QLabel(self.malsman)
        self.telefonlb_mm.setObjectName("telefonlb_mm")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.telefonlb_mm)
        self.telefon_mm = QtWidgets.QLineEdit(self.malsman)
        self.telefon_mm.setObjectName("telefon_mm")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.telefon_mm)
        self.verticalLayout.addWidget(self.malsman)
        self.buttonBox = QtWidgets.QDialogButtonBox(NyMedlem)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(NyMedlem)
        self.kon.setCurrentIndex(-1)
        self.group.setCurrentIndex(-1)
        self.buttonBox.accepted.connect(NyMedlem.accept)
        self.buttonBox.rejected.connect(NyMedlem.reject)
        QtCore.QMetaObject.connectSlotsByName(NyMedlem)
        NyMedlem.setTabOrder(self.namn, self.pers_num)
        NyMedlem.setTabOrder(self.pers_num, self.kon)
        NyMedlem.setTabOrder(self.kon, self.email)
        NyMedlem.setTabOrder(self.email, self.telefon)
        NyMedlem.setTabOrder(self.telefon, self.adress)
        NyMedlem.setTabOrder(self.adress, self.post_num)
        NyMedlem.setTabOrder(self.post_num, self.ort)
        NyMedlem.setTabOrder(self.ort, self.group)
        NyMedlem.setTabOrder(self.group, self.betalt)
        NyMedlem.setTabOrder(self.betalt, self.namn_mm)
        NyMedlem.setTabOrder(self.namn_mm, self.email_mm)
        NyMedlem.setTabOrder(self.email_mm, self.telefon_mm)
        NyMedlem.setTabOrder(self.telefon_mm, self.kommentar)

    def retranslateUi(self, NyMedlem):
        _translate = QtCore.QCoreApplication.translate
        NyMedlem.setWindowTitle(_translate("NyMedlem", "NyMedlem"))
        self.ID_lb.setText(_translate("NyMedlem", "ID:"))
        self.ID_val.setText(_translate("NyMedlem", "None"))
        self.namn_id.setText(_translate("NyMedlem", "Namn:"))
        self.namn.setPlaceholderText(_translate("NyMedlem", "Namn Efternamn"))
        self.pers_num_lb.setText(_translate("NyMedlem", "Personnummer:"))
        self.pers_num.setInputMask(_translate("NyMedlem", "99999999-9999"))
        self.kon_lb.setText(_translate("NyMedlem", "Kön:"))
        self.kon.setItemText(0, _translate("NyMedlem", "Man"))
        self.kon.setItemText(1, _translate("NyMedlem", "Kvinna"))
        self.kon.setItemText(2, _translate("NyMedlem", "Okänd"))
        self.email_lb.setText(_translate("NyMedlem", "Email:"))
        self.email.setPlaceholderText(_translate("NyMedlem", "någon@email.se"))
        self.adress_lb.setText(_translate("NyMedlem", "Adress:"))
        self.adress.setPlaceholderText(_translate("NyMedlem", "Tellusgatan 15"))
        self.postnum_lb.setText(_translate("NyMedlem", "Postnummer:"))
        self.post_num.setInputMask(_translate("NyMedlem", "999 99"))
        self.post_num.setPlaceholderText(_translate("NyMedlem", "224 57"))
        self.ort_lb.setText(_translate("NyMedlem", "Ort:"))
        self.ort.setPlaceholderText(_translate("NyMedlem", "Lund"))
        self.grupp_lb.setText(_translate("NyMedlem", "Grupp:"))
        self.group.setItemText(0, _translate("NyMedlem", "Basic"))
        self.group.setItemText(1, _translate("NyMedlem", "Intermidiate"))
        self.group.setItemText(2, _translate("NyMedlem", "Advanced"))
        self.group.setItemText(3, _translate("NyMedlem", "Kids"))
        self.group.setItemText(4, _translate("NyMedlem", "Tävling"))
        self.Betalt_lb.setText(_translate("NyMedlem", "Betalt:"))
        self.betalt.setText(_translate("NyMedlem", "Ja"))
        self.kommentar_lb.setText(_translate("NyMedlem", "Kommentar:"))
        self.telefon_lb.setText(_translate("NyMedlem", "Telefon:"))
        self.malsman.setTitle(_translate("NyMedlem", "Målsman"))
        self.namnlb_mm.setText(_translate("NyMedlem", "Namn:"))
        self.emaillb_mm.setText(_translate("NyMedlem", "Email:"))
        self.telefonlb_mm.setText(_translate("NyMedlem", "Telefon:"))
