from PyQt5 import QtWidgets, QtCore
from rf_entry_ui import Ui_RF_Entry
from ny_dialog_ui import Ui_NyMedlem
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
    sig = QtCore.pyqtSignal(int)

    def __init__(self):
        super(BarReader, self).__init__()

        # Connect signal to the desired function
        self.sig.connect(updateProgBar)

    def run(self):
        while True:
            val = sysInfo.getCpu()

            # Emit the signal
            self.sig.emit(val)
# DataBase thread


class RF_Entry(QtWidgets.QMainWindow):
    def __init__(self):
        super(RF_Entry, self).__init__()
        self.ui = Ui_RF_Entry()
        self.ui.setupUi(self)

        # Connections
        self.ui.startButton.toggled.connect(self.StartLog)
        # Start Members class and Visitor class

    def StartLog(self):
        if self.ui.startButton.text() == "Start":
            self.ui.startButton.setText("Stop")
            # Launch Logging
        else:
            self.ui.startButton.setText("Start")
            # Stopp Logging


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = RF_Entry()
    application.show()
    sys.exit(app.exec())
