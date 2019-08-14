from PyQt5 import QtWidgets, QtCore
from rf_entry_ui import Ui_RF_Entry
import sys
# import os

# Member class

# Add/Edit Member dialog separate Thread

# Export CSV dialog

# Settings dialog

# Bar Scanner Thread

# DataBase thread


class RF_Entry(QtWidgets.QMainWindow):
    def __init__(self):
        super(RF_Entry, self).__init__()
        self.ui = Ui_RF_Entry()
        self.ui.setupUi(self)

        # Connections
        self.ui.startButton.toggled.connect(self.StartLog)

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
