import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont #Este comando permite cambiar la fuente de los labels
from PyQt5.QtCore import Qt #Con este comando se pueden alinear los objetos

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()  #Este es el constructor
        self.setWindowTitle('Mi segundo intento en GUI con PyQt') #Con este comando se ubica el título
        self.setGeometry(700,350,500,500) #Los argumentos indican donde se va a ubicar (pos x, pos y, ancho, alto)

        label = QLabel('Hola', self)
        label.setFont(QFont('Arial', 40))
        label.setGeometry(0,0,500,100) #Los argumentos indican donde se va a ubicar (pos x, pos y, ancho, alto)
        label.setStyleSheet("color:blue;"
                            "background-color:red;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") #De esta manera se pueden cambiar el color de los objetos, similar a CSS
        # label.setAlignment(Qt.AlignTop) #Alineado verticalmente arriba
        # label.setAlignment(Qt.AlignBottom)  # Alineado  verticalmente abajo
        #label.setAlignment(Qt.AlignVCenter)  # Alineado verticalmente al centro
        #label.setAlignment(Qt.AlignRight) # Alineado horizontalmente a la derecha
        #label.setAlignment(Qt.AlignLeft) # Alineado horizontalmente a la izquierda
        #label.setAlignment(Qt.AlignHCenter) # Alineado horizontalmente en el medio
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #El operador | permite manejar ambas alineaciones en una única linea
        label.setAlignment(Qt.AlignCenter) #Así es como se alinea en el medio

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() #El metodo show muestra por un momento la ventana creada
    sys.exit(app.exec_()) #Con el metodo usado aqui se ejecuta la aplicación

if __name__ ==  "__main__":
    main()
