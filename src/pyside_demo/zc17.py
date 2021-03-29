from PySide6.QtWidgets import QPushButton, QMainWindow, QApplication
import sys


class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        btn1.move(30, 50)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Event sender")

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " was pressed")


def main():
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
