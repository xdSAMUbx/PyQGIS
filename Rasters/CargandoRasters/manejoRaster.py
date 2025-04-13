"""
Este código tiene el objetivo de darle manejo propio al raster, obtener por lo menos de una única banda los valores
en forma de matriz, estádisticas a partir de las propiedades de la capa que nos brinda qgis facilmente
"""
# Librerias y software de QGIS
from pathlib import Path
from qgis.core import (
    QgsApplication,
    QgsProject,
    QgsRasterLayer,
)

# Librerias de Python
import pandas as pd
import numpy as np

def startingProject () -> None:

    QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.40.5/apps/qgis-ltr", True)
    qgis = QgsApplication ([],True)

    try:
        qgis.initQgis()

    except Exception as ex:
        print(f"Ocurrio el siguiente error: {ex}")
        return

    finally:
        qgis.exitQgis()

if __name__ == "__main__":
    startingProject()