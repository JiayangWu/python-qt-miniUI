import sys

from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        btn.resize(btn.sizeHint())

        btn.move(150, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This is a <b>Quit</b> button!')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
