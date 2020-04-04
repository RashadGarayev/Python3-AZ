# kitabxanaları proqrama daxil edirik
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, webbrowser

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Əsas pəncərə self ifadəsində referans alındı.
        self.setWindowTitle("Bu mənim ilk proqramım")
        # Pəncərə loqosu
        self.setWindowIcon(QIcon('../image/ico.png'))  # Pəncərə sol yuxarı küncdə loqo əlavə olundu
        # Pəncərə arxa plan rəngi
        self.palette = QPalette()
        self.palette.setColor(QPalette.Background, Qt.white)
        self.setPalette(self.palette)
        self.spinbox = QSpinBox()
        self.label = QLabel('Spinbox value:')
        self.spinbox.resize(100, 25)
        self.spinbox.setRange(1994, 2009)
        self.spinbox.setValue(200)
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.spinbox)
        self.grid.addWidget(self.label)
        self.spinbox.valueChanged.connect(self.create)
        self.show()

    def create(self):
        self.label.setText('Value:' + str(self.spinbox.value()))
if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    app.exec_()