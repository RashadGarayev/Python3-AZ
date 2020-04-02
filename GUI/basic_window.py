from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

def Pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    sys.exit(app.exec_())
Pencere()