import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon (Este comando permite establecer iconos en nuestra aplicación)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()  #Este es el constructor
        self.setWindowTitle('Mi primer intento en GUI con PyQt') #Con este comando se ubica el título
        self.setGeometry(700,350,500,500) #Los argumentos indican donde se va a ubicar (pos x, pos y, ancho, alto)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() #El metodo show muestra por un momento la ventana creada
    sys.exit(app.exec_()) #Con el metodo usado aqui se ejecuta la aplicación

if __name__ ==  "__main__":
    main()
