# kitabxanaları proqrama daxil edirik
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, time
var1 =time.time()
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
        self.button = QPushButton(self)
        self.button.setText(u'Başla')
        self.button.setIcon(QIcon('../image/bstart.png'))
        self.button.move(220,50)
        self.button.clicked.connect(self.Speed)
        self.show()
    def Speed(self):
        var2 = time.time()
        delta = var1-var2
        self.label = QLabel(self)
        self.label.setText('{} saniyə'.format(str(delta)))
        self.label.move(220,80)
        self.label.show()



if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    app.exec_()