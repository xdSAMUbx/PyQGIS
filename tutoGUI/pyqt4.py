import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.button = QPushButton("click me",self)
        self.label = QLabel('Hola',self)
        self.vbox = QVBoxLayout()
        self.centralWidget = QWidget()
        self.initGUI()

    def initGUI(self) -> None:
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet('font-size: 30px;')
        self.button.clicked.connect(self.onClick)

        self.label.setGeometry(150,200,200,100)
        self.label.setStyleSheet('font-size: 50px;')

        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.label)
        self.centralWidget.setLayout(self.vbox)

    def onClick(self) -> None:
        print('Button clicked')
        self.button.setText('Clicked')
        self.button.setDisabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
