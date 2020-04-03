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
        self.label = QLabel(self)
        self.label.setText(u'Adınız')
        self.label.move(150,50)

        self.lineedit = QLineEdit(self)
        self.lineedit.setAlignment(Qt.AlignLeft)
        self.lineedit.move(200, 50)

        self.label1 = QLabel(self)
        self.label1.setText((u'Yaşınız'))
        self.label1.move(150,80)
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setInputMask('99')
        self.lineedit1.setAlignment(Qt.AlignLeft)
        self.lineedit1.move(200,80)
        self.button = QPushButton(self)
        self.button.setText(u'click')
        self.button.move(230,100)
        self.button.clicked.connect(self.goster)
        self.show()
    def goster(self):
        print('Adım :{} | Yaşım :{}'.format(self.lineedit.text(),self.lineedit1.text()))

if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    app.exec_()