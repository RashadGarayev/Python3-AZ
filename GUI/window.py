# kitabxanaları proqrama daxil edirik
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #Əsas pəncərə self ifadəsində referans alındı.
        self.setWindowTitle("Bu mənim ilk proqramım")
        #Pəncərə loqosu
        self.setWindowIcon(QIcon('../image/ico.png')) #Pəncərə sol yuxarı küncdə loqo əlavə olundu
        #Pəncərə arxa plan rəngi
        self.palette = QPalette()
        self.palette.setColor(QPalette.Background,Qt.white)
        self.setPalette(self.palette)
        self.label = QLabel(self) #self ifadəsi MainWindow pəncərədə olduğunu təmsil edir
        #self.label.setText('Pyqt Dərsləri')
        self.label.setText("<font color='Blue'>PyQt dərsləri</font>")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

app = QApplication(sys.argv)
window = MainWindow()
window.show() #Pəncərənin göstərilməsi
# Proqramın davamlı göstərilməsi
app.exec_()