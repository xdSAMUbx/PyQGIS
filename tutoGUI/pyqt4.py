import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.button = QPushButton("click me",self)
        self.label = QLabel('Hola',self)
        self.vbox = QVBoxLayout(self)
        self.centralWidget = QWidget(self)
        self.initGUI()

    def initGUI(self) -> None:

        self.button.setStyleSheet('font-size: 30px;')
        self.button.clicked.connect(self.onClick)  #Se debe revisar los eventos al interactuar con teclado y raton

        self.label.setStyleSheet('font-size: 50px;')

        self.vbox.addWidget(self.button, alignment = Qt.AlignCenter)
        self.vbox.addWidget(self.label, alignment = Qt.AlignCenter)

        self.centralWidget.setLayout(self.vbox)
        self.setCentralWidget(self.centralWidget)

    def onClick(self) -> None:
        self.label.setText('Adiós')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
