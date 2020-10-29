import sys

from PyQt5 import QtWidgets
from UI.login import Ui_PACHE

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PACHE = QtWidgets.QMainWindow()
    ui = Ui_PACHE()
    ui.setupUi(PACHE)
    PACHE.show()
    sys.exit(app.exec_())