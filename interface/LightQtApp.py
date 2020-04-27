from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
import sys
import functions.lan_functions as lan_functions


def test():
    print(lan_functions.discover_lights())


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(600, 300, 300, 500)
    win.setFixedSize(300, 500)

    label = QLabel(win)
    label.setText('Label one')
    label.move(50, 50)

    btn1 = QPushButton(win)
    btn1.setText('Click here')
    btn1.clicked.connect(test)

    win.setWindowTitle('Test')
    win.show()
    sys.exit(app.exec_())

window()