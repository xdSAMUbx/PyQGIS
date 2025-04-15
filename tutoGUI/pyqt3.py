import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()

    def initUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        label1 = QLabel("#1",self)
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)

        label1.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:yellow;")
        label3.setStyleSheet("background-color:green;")
        label4.setStyleSheet("background-color:blue;")
        """
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        
        De esta manera se pueden ordenar los items dentro de la GUI que estamos buscando hacer, de tal forma que si es
        H será horizontal, si es V sera vertical y si es Grid, formara una grilla para ubicarla
        """
        grid = QGridLayout()
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,1,0)
        grid.addWidget(label4,1,1)

        centralWidget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()