import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QDesktopWidget,
                             QGridLayout, QGroupBox)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # -------------------------------Grupos de la Interfaz-------------------------------
        self.grid = QGridLayout()

        # Primer grupo ocupará 2 filas y 1 columna
        self.grid.addWidget(self.primerGrupo(), 0, 0, 1, 2)  # (fila, columna, filas ocupadas, columnas ocupadas)

        # Segundo grupo ocupará 1 fila y 2 columnas
        self.grid.addWidget(self.segundoGrupo(), 1, 0, 2, 2)

        # Tercer grupo ocupará 2 filas y 1 columna
        self.grid.addWidget(self.tercerGrupo(), 0, 2, 2, 1)

        # Cuarto grupo ocupará 1 fila y 1 columna
        self.grid.addWidget(self.cuartoGrupo(), 2, 2, 1, 1)

        # Asignamos el layout a la ventana
        central_widget = QWidget(self)  # Crear un widget central
        central_widget.setLayout(self.grid)
        self.setCentralWidget(central_widget)

        # -------------------------------Geometría de la interfaz----------------------------
        # Obtener la geometría de la pantalla primaria
        self.screen = QDesktopWidget().screenGeometry(0)

        # Establecer la geometría de la ventana centrada en la pantalla
        ventana_width = 1000
        ventana_height = 700
        x_pos = (self.screen.width() - ventana_width) // 2  # Centrado en X
        y_pos = (self.screen.height() - ventana_height) // 2  # Centrado en Y

        # Establecer la geometría de la ventana con posición y tamaño
        self.setGeometry(x_pos, y_pos, ventana_width, ventana_height)

    def primerGrupo(self):
        group_box = QGroupBox("Primer Grupo")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Botón 1"))
        group_box.setLayout(layout)
        return group_box

    def segundoGrupo(self):
        group_box = QGroupBox("Segundo Grupo")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Botón 2"))
        group_box.setLayout(layout)
        return group_box

    def tercerGrupo(self):
        group_box = QGroupBox("Tercer Grupo")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Botón 3"))
        group_box.setLayout(layout)
        return group_box

    def cuartoGrupo(self):
        group_box = QGroupBox("Cuarto Grupo")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Botón 4"))
        group_box.setLayout(layout)
        return group_box


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
