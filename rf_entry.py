#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox as QMB
from rf_entry_ui import Ui_RF_Entry
from ny_dialog_ui import Ui_NyMedlem
# from bet_dialog_ui import Ui_Betalat
import serial
import datetime as dt
from serial.serialutil import SerialException
import sqlite3
import time
import sys
import re

# import os
# Export CSV dialog
# Settings dialog
# Bar Scanner Thread


class BarReader(QtCore.QThread):
    code = QtCore.pyqtSignal(int)

    def __init__(self, settings=None):
        super(BarReader, self).__init__()
        self.ser = None
        self.done = False

    def connect(self):
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1,
                                     parity=serial.PARITY_EVEN, rtscts=1,
                                     bytesize=8)
            return True
        except SerialException as err:
            if err.errno==2:
                print("Cant connect to {}".format(err.strerror))
                sys.exit(99)
            elif err.errno==16:
                print("Device  busy, try again")
                return False

    def __del__(self):
        if self.ser:
            self.ser.close()
        self.wait()

    def stop(self):
        self.done = True
        if self.ser:
            self.ser.close()

    def run(self):
        self.done = False
        while(not self.connect()):
            time.sleep(2)
        self.ser.flush()
        while not self.done:
            val = self.ser.readline()
            if val:
                try:
                    self.code.emit(int(val))
                except ValueError:
                    # Handle
                    pass


# DataBase thread
class MembersDB:
    def __init__(self, members_db=None):
        # Open database of members
        self.conn_M = sqlite3.connect("members.db")
        self.curs_M = self.conn_M.cursor()
        self.curs_M.executescript("""
            CREATE TABLE if not exists members (
                time DATETIME DEFAULT (datetime('now','localtime')),
                ID INTEGER PRIMARY_KEY,
                namn,
                persnum,
                kon,
                email,
                telefon,
                adress,
                postnum,
                ort,
                grupp,
                betalt BIT,
                kommentar,
                namn_mm,
                email_mm,
                telefon_mm);""")
        self.conn_M.commit()
        self.conn_V = sqlite3.connect("visits.db")
        self.curs_V = self.conn_V.cursor()
        self.curs_V.executescript("""
            CREATE TABLE if not exists visits (
                time DATETIME DEFAULT (datetime('now','localtime')),
                ID INTEGER PRIMARY_KEY,
                pass);""")
        self.conn_V.commit()

    def logVisit(self, ID, tpass):
        sql = """
        INSERT INTO visits (ID,pass)
        VALUES ({},'{}')
        """.format(ID, tpass)
        self.curs_V.execute(sql)
        self.conn_V.commit()

        sql = "SELECT namn, grupp, betalt FROM members where ID={}".format(ID)
        return self.curs_M.execute(sql).fetchone()[0:3]

    def addMember(self, member=None):
        if member:
            sql = """
            INSERT INTO members (ID,namn,persnum,kon,email,telefon,adress,postnum,ort,grupp,betalt,kommentar,namn_mm,email_mm,telefon_mm)
            VALUES ({ID},'{namn}','{persnum}','{kon}','{email}','{telefon}','{adress}','{postnum}','{ort}','{grupp}',{betalt},'{kommentar}','{namn_mm}','{email_mm}','{telefon_mm}');
            """.format(**member)
            self.curs_M.execute(sql)
            self.conn_M.commit()

    def updateMember(self, member=None):
        if member:
            sql = """
            UPDATE members
            SET namn='{namn}',persnum='{persnum}',kon='{kon}',email='{email}',telefon='{telefon}',adress='{adress}',postnum='{postnum}',ort='{ort}',grupp='{grupp}',betalt={betalt},kommentar='{kommentar}',namn_mm='{namn_mm}',email_mm='{email_mm}',telefon_mm='{telefon_mm}'
            WHERE ID={ID};
            """.format(**member)
            self.curs_M.execute(sql)
            self.conn_M.commit()

    def isMember(self, ID):
        sql = "select exists(select 1 from members where ID={}) limit 1".format(ID)
        ret = self.curs_M.execute(sql)
        if ret.fetchone()[0] == 0:
            return False
        else:
            return True

    def fetchMember(self, ID):
        sql = "SELECT namn,persnum,kon,email,telefon,adress,postnum,ort,grupp,betalt,kommentar,namn_mm,email_mm,telefon_mm FROM members where ID={}".format(ID)
        keys = ['namn','persnum','kon','email','telefon','adress','postnum','ort','grupp','betalt','kommentar','namn_mm','email_mm','telefon_mm']
        val = self.curs_M.execute(sql).fetchone()
        return dict(zip(keys, val))

    def setPaid(self, ID, bet='Nej'):
        if bet == 'Nej':
            val = 0
        elif bet == 'Ja':
            val = 1
        else:
            val = 0
        sql = """UPDATE members
                 SET betalt={1}
                 WHERE ID={0}""".format(ID, val)
        self.curs_M.execute(sql)
        self.conn_M.commit()


class AddMember(QtWidgets.QDialog):
    def __init__(self, ID, member=None):
        super(AddMember, self).__init__()
        self.ui = Ui_NyMedlem()
        self.ui.setupUi(self)
        self.ui.ID_val.setText(str(ID))
        self.ID = ID
        self.ui.pers_num.editingFinished.connect(self.checkAge)
        self.ui.namn.editingFinished.connect(self.validData)
        self.ui.pers_num.editingFinished.connect(self.validData)
        self.ui.email.editingFinished.connect(self.validData)
        self.ui.telefon.editingFinished.connect(self.validData)
        self.ui.adress.editingFinished.connect(self.validData)
        self.ui.post_num.editingFinished.connect(self.validData)
        self.ui.ort.editingFinished.connect(self.validData)
        self.ui.namn_mm.editingFinished.connect(self.validData)
        self.ui.telefon_mm.editingFinished.connect(self.validData)
        self.ui.email_mm.editingFinished.connect(self.validData)
        self.ui.group.currentIndexChanged.connect(self.validData)
        if member:
            self.ui.namn.setText(member['namn'])
            self.ui.pers_num.setText(member['persnum'])
            idx = self.ui.kon.findText(member['kon'])
            self.ui.kon.setCurrentIndex(idx)
            self.ui.email.setText(member['email'])
            self.ui.telefon.setText(member['telefon'])
            self.ui.adress.setText(member['adress'])
            self.ui.post_num.setText(member['postnum'])
            self.ui.ort.setText(member['ort'])
            idx = self.ui.group.findText(member['grupp'])
            self.ui.group.setCurrentIndex(idx)
            self.ui.betalt.setChecked(member['betalt'])
            self.ui.kommentar.setText(member['kommentar'])
            if member['namn_mm']:
                self.ui.malsman.setEnabled(True)
                self.ui.namn_mm.setText(member['namn_mm'])
                self.ui.email_mm.setText(member['email_mm'])
                self.ui.telefon_mm.setText(member['telefon_mm'])

    def validData(self):
        if self.ui.malsman.isEnabled():
            if self.ui.namn.text() and self.ui.pers_num.text() and\
               self.ui.email.text() and self.ui.telefon.text() and\
               self.ui.adress.text() and self.ui.post_num.text() and\
               self.ui.ort.text() and self.ui.namn_mm.text() and\
               self.ui.email_mm.text() and self.ui.telefon_mm.text() and self.ui.group.currentText():
               self.ui.buttonBox.setEnabled(True)
               return
        elif self.ui.namn.text() and self.ui.pers_num.text() and\
             self.ui.email.text() and self.ui.telefon.text() and\
             self.ui.adress.text() and self.ui.post_num.text() and\
             self.ui.ort.text() and self.ui.group.currentText():
           self.ui.buttonBox.setEnabled(True)
           return
        #    if self.ui.malsman.isEnabled()
        # self.ui.namn_mm.text()
        # self.ui.telefon_mm.text()
        # self.ui.email_mm.text()

    def checkAge(self):
        """ Kolla om giltigt personnummer, samt kolla kön och ålder """
        pnr = self.ui.pers_num.text()
        digits = [int(d) for d in re.sub(r'\D', '', pnr)][-10:]
        if len(digits) != 10:
            diag = QMB.warning(self,"Ogiltigt personnummer",pnr)
            self.ui.pers_num.clear()
            return
        even_digitsum = sum(x if x < 5 else x - 9 for x in digits[::2])
        valid = 0 == sum(digits, even_digitsum) % 10
        if not valid:
            diag = QMB.warning(self,"Ogiltigt personnummer",pnr)
            self.ui.pers_num.clear()
            return
        if digits[-2]%2==0:
            self.ui.kon.setCurrentIndex(1)
        else:
            self.ui.kon.setCurrentIndex(0)

        bday = dt.datetime.strptime(self.ui.pers_num.text().split('-')[0],"%Y%m%d")
        tday = dt.datetime.today()
        age = int((tday-bday).days/365)
        if age < 18:
            self.ui.malsman.setEnabled(True)
        else:
            self.ui.malsman.setDisabled(True)

    def getMember(self):
        namn = self.ui.namn.text()
        persnum = self.ui.pers_num.text()
        kon = self.ui.kon.currentText()
        email = self.ui.email.text()
        telefon = self.ui.telefon.text()
        adress = self.ui.adress.text()
        postnum = self.ui.post_num.text()
        ort = self.ui.ort.text()
        grupp = self.ui.group.currentText()
        betalt = int(self.ui.betalt.isChecked())
        kommentar = self.ui.kommentar.toPlainText()
        namn_mm = self.ui.namn_mm.text()
        email_mm = self.ui.email_mm.text()
        telefon_mm = self.ui.telefon_mm.text()

        return {'ID': self.ID, 'namn': namn, 'persnum': persnum, 'kon': kon,
                'email': email, 'telefon': telefon, 'adress': adress,
                'postnum': postnum, 'ort': ort, 'grupp': grupp,
                'betalt': betalt, 'kommentar': kommentar,'namn_mm': namn_mm,
                'email_mm': email_mm, 'telefon_mm': telefon_mm}


class RF_Entry(QtWidgets.QMainWindow):
    def __init__(self):
        super(RF_Entry, self).__init__()
        self.ui = Ui_RF_Entry()
        self.ui.setupUi(self)
        self.ui.startButton.setDisabled(True)
        self.memberDB = MembersDB()

        self.barReader = BarReader()

        # Connections
        self.ui.startButton.clicked.connect(self.StartLog)
        # self.ui.clearButton.clicked.connect(self.ClearLog)
        self.ui.tgroup.currentIndexChanged.connect(self.OnGroup)
        self.ui.actionQuit.triggered.connect(self.OnQuit)
        self.ui.reportWindow.cellDoubleClicked.connect(self.OnCell)
        self.barReader.code.connect(self.OnCode)
        # Start Members class and Visitor class

    def OnGroup(self):
        self.ui.startButton.setEnabled(True)

    def ClearLog(self):
        """ Clear the entire log """
        while(self.ui.reportWindow.rowCount() != 0):
            self.ui.reportWindow.removeRow(0)

    def OnCell(self, r, c):
        ID = int(self.ui.reportWindow.verticalHeaderItem(r).text())
        member = self.memberDB.fetchMember(ID)
        if c == 1:
            # Dialog fråga om betalat
            diag = QMB.question(self, "Betalat?", "Har {} betalat?".format(member['namn']),
                                QMB.Yes | QMB.No, QMB.Yes)
            if diag == QMB.Yes:
                self.ui.reportWindow.setItem(r, c, QTableWidgetItem("Ja"))
                self.memberDB.setPaid(ID, 'Ja')
            else:
                self.ui.reportWindow.setItem(r, c, QTableWidgetItem("Nej"))
                self.memberDB.setPaid(ID, 'Nej')
        elif c == 2:
            diag = AddMember(ID, member)
            if diag.exec_():
                mber = diag.getMember()
                self.memberDB.updateMember(mber)
                self.ui.reportWindow.setItem(r, 0, QTableWidgetItem(mber['grupp']))
                self.ui.reportWindow.setItem(r, 1, QTableWidgetItem("Ja" if mber['betalt'] else "Nej"))
                self.ui.reportWindow.setItem(r, 2, QTableWidgetItem(mber['namn']))
        else:
            # Ingen funktion
            pass

    def StartLog(self):
        # This happens on start
        if self.ui.startButton.text() == "Start":
            self.ClearLog()
            self.ui.startButton.setText("Stop")
            self.ui.startButton.setStyleSheet('background-color: red')
            self.ui.tgroup.setDisabled(True)
            # Launch BarReader
            self.barReader.start()
        # This hapens when stop
        else:
            self.ui.startButton.setText("Start")
            self.ui.startButton.setStyleSheet('background-color: lightgray')
            self.ui.tgroup.setCurrentIndex(-1)
            self.ui.tgroup.setEnabled(True)
            self.ui.startButton.setDisabled(True)
            # Stopp BarReader
            self.barReader.stop()

    # def _determineGroup(self):
    #     """ Determine what group the member intend to train in """
    #     now = dt.datetime.today()
    #     wday = now.weekday()
    #     basic_t = dt.datetime(now.year, now.month, now.day, hour=17, minute=00)
    #     interm_t = dt.datetime(now.year, now.month, now.day, hour=18, minute=00)
    #     if wday in [0, 2, 4] and (basic_t - now).seconds < 2400 and (now-basic_t).seconds < 900:
    #         return 'Basic'
    #     elif wday in [0, 2] and (interm_t - now).seconds < 2400 and (now-interm_t).seconds < 900:
    #         return 'Intermidiate'
    #     else:
    #         return None

    def OnCode(self, code):
        if code < 0 or code > 400:
            return
        if self.memberDB.isMember(code):
            member = self.memberDB.fetchMember(code)
            IDS=[]
            for row in range(self.ui.reportWindow.rowCount()):
                IDS.append(int(self.ui.reportWindow.verticalHeaderItem(row).text()))
            if code in IDS:
                return
            if member['grupp'] == "Tävling":
                n, g, b = self.memberDB.logVisit(code, "Tävling")
            else:
                n, g, b = self.memberDB.logVisit(code, self.ui.tgroup.currentText())
            row = self.ui.reportWindow.rowCount()
            self.ui.reportWindow.insertRow(row)
            self.ui.reportWindow.setVerticalHeaderItem(row, QTableWidgetItem(str(code)))
            self.ui.reportWindow.setItem(row, 0, QTableWidgetItem(g))
            self.ui.reportWindow.setItem(row, 1, QTableWidgetItem("Ja" if b else "Nej"))
            self.ui.reportWindow.setItem(row, 2, QTableWidgetItem(n))
        else:
            diag = AddMember(code)
            if diag.exec_():
                member = diag.getMember()
                self.memberDB.addMember(member)

    def OnQuit(self):
        self.memberDB.conn_M.commit()
        self.memberDB.conn_V.commit()
        self.barReader.stop()
        sys.exit(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = RF_Entry()
    application.show()
    sys.exit(app.exec())
