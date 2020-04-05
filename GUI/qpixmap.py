# kitabxanaları proqrama daxil edirik
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

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
        self.setGeometry(400,400,600,600)
        self.setFixedSize(600,600)
        self.tab = QTabWidget(self)
        self.tab.setGeometry(0,30,500,450)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab.addTab(self.tab1, 'Tab-1')
        self.tab.addTab(self.tab2, 'Tab-2')
        self.toolbar = QToolBar(self)
        self.toolbar.addAction('File')
        self.toolbar.addAction('Open')
        self.toolbar.setMovable(False)
        self.show()
if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    app.exec_()