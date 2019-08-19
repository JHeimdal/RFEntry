from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from rf_entry_ui import Ui_RF_Entry
from ny_dialog_ui import Ui_NyMedlem
import serial
from serial.serialutil import SerialException
import sqlite3

import sys
# import os

# Member class
class Member:
    def __init__(self):
        self.name = None
        self.pernum = None
        self.adress = None
        self.postnum = None
        self.ort = None
        self.group = None
        self.payed = False
        self.ID = None
        self.comment = None

# Add/Edit Member dialog separate Thread

# Export CSV dialog

# Settings dialog

# Bar Scanner Thread
class BarReader(QtCore.QThread):
    code = QtCore.pyqtSignal(int)

    def __init__(self, settings=None):
        super(BarReader, self).__init__()
        self.done = False

    def connect(self):
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1,
                                     parity=serial.PARITY_EVEN, rtscts=1,
                                     bytesize=8)
        except SerialException as err:
            pass

    def __del__(self):
        self.ser.close()
        self.wait()

    def stop(self):
        self.done = True
        self.ser.close()

    def run(self):
        self.done = False
        self.connect()
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
                adress,
                postnum,
                ort,
                grupp,
                betalt BIT,
                kommentar);""")
        self.conn_M.commit()
        self.conn_V = sqlite3.connect("visits.db")
        self.curs_V = self.conn_V.cursor()
        self.curs_V.executescript("""
            CREATE TABLE if not exists visits (
                time DATETIME DEFAULT (datetime('now','localtime')),
                ID INTEGER PRIMARY_KEY,
                pass);""")
        self.conn_V.commit()


    def logVisit(self, ID):
        sql = """
        INSERT INTO visits (ID,pass)
        VALUES ({},'{}')
        """.format(ID,"pass")
        self.curs_V.execute(sql)
        self.conn_V.commit()

        sql = "SELECT namn, grupp, betalt FROM members where ID={}".format(ID)
        return self.curs_M.execute(sql).fetchone()[0:3]


    def addMember(self, member=None):
        if member:
            sql = """
            INSERT INTO members (ID,namn,persnum,kon,email,adress,postnum,ort,grupp,betalt,kommentar)
            VALUES ({ID},'{namn}','{persnum}','{kon}','{email}','{adress}','{postnum}','{ort}','{grupp}',{betalt},'{kommentar}')
            """.format(**member)
            self.curs_M.execute(sql)
            self.conn_M.commit()

    def isMember(self, ID):
        sql = "select exists(select 1 from members where ID={}) limit 1".format(ID)
        ret = self.curs_M.execute(sql)
        if ret.fetchone()[0]==0:
            return False
        else:
            return True

class AddMember(QtWidgets.QDialog):
    def __init__(self, ID):
        super(AddMember, self).__init__()
        self.ui = Ui_NyMedlem()
        self.ui.setupUi(self)
        self.ui.ID_val.setText(str(ID))
        self.ID = ID

    def getMember(self):
        namn = self.ui.namn.text()
        persnum = self.ui.pers_num.text()
        kon = self.ui.kon.currentText()
        email = self.ui.email.text()
        adress = self.ui.adress.text()
        postnum = self.ui.post_num.text()
        ort = self.ui.ort.text()
        grupp = self.ui.group.currentText()
        betalt = self.ui.betalt.isChecked()
        kommentar = self.ui.kommentar.toPlainText()

        return {'ID':self.ID, 'namn':namn, 'persnum':persnum, 'kon':kon,
                'email':email, 'adress':adress, 'postnum':postnum, 'ort':ort,
                'grupp':grupp, 'betalt':betalt, 'kommentar':kommentar}


class RF_Entry(QtWidgets.QMainWindow):
    def __init__(self):
        super(RF_Entry, self).__init__()
        self.ui = Ui_RF_Entry()
        self.ui.setupUi(self)

        self.memberDB = MembersDB()

        self.barReader = BarReader()

        # Connections
        self.ui.startButton.toggled.connect(self.StartLog)
        self.barReader.code.connect(self.OnCode)
        # Start Members class and Visitor class

    def StartLog(self):
        if self.ui.startButton.text() == "Start":
            self.ui.startButton.setText("Stop")
            # Launch BarReader
            self.barReader.start()
        else:
            self.ui.startButton.setText("Start")
            # Stopp BarReader
            self.barReader.stop()

    def OnCode(self, code):
        if self.memberDB.isMember(code):
            n, g, b = self.memberDB.logVisit(code)
            if b:
                bet = "Ja"
            else:
                bet = "Nej"
            row = self.ui.reportWindow.rowCount()
            self.ui.reportWindow.insertRow(row)
            self.ui.reportWindow.setItem(row,0,QTableWidgetItem(g))
            self.ui.reportWindow.setItem(row,1,QTableWidgetItem(bet))
            self.ui.reportWindow.setItem(row,2,QTableWidgetItem(n))
            # ret = self.memberDB.logVisit(code)
        else:
            diag = AddMember(code)
            if diag.exec_():
                member = diag.getMember()
                self.memberDB.addMember(member)
            else:
                print("E")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = RF_Entry()
    application.show()
    sys.exit(app.exec())
