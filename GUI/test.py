from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys
def pencere():
    app=QApplication(sys.argv)
    window=QWidget()
    window.setGeometry(400,300,256,256)
    window.setWindowTitle('Hello PyQt')
    label=QLabel(window)
    photo=QPixmap('../image/ai.jpg') #və ya ('/home/user/Picture/icon.png')
    label.setPixmap(photo)
    label.show()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    pencere()