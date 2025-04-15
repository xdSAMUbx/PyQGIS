import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__ (self) -> None:
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.vbox = QVBoxLayout(self)
        self.centralWidget = QWidget(self)
        self.lineEdit = QLineEdit(self)
        self.button = QPushButton('Submit', self)
        self.initGUI()

    def initGUI(self) -> None:
        self.vbox.addWidget(self.lineEdit, alignment = Qt.AlignCenter)
        self.vbox.addWidget(self.button, alignment = Qt.AlignCenter)
        self.centralWidget.setLayout(self.vbox)
        self.setCentralWidget(self.centralWidget)


        self.lineEdit.setStyleSheet('font-size: 25px;'
                                    'font-family: Arial;')
        self.button.setStyleSheet('font-size: 25px;'
                                  'font-family: Arial;')
        self.lineEdit.setPlaceholderText('Ingresa tu nombre')
        self.button.clicked.connect(self.submit)

    def submit(self) -> None:
        text = self.lineEdit.text()
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())