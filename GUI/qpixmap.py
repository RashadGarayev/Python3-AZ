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
        self.setGeometry(600,150,512,512)
        self.label=QLabel(self)
        self.pixmap = QPixmap('../image/ai.png')
        self.label.setPixmap(self.pixmap)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    app.exec_()