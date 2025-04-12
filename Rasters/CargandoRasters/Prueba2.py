import os
from qgis.core import QgsApplication, QgsProject, QgsRasterLayer
from qgis.gui import QgsMapCanvas

"""
Este programa esta creado con el fin de ser la continuación de la Prueba1 generada anteriormente donde se busca
realizar el paso a paso para cargar una capa Raster sin necesidad de abrir QGIS
"""
def importarRaster () -> None:

    """
    Esta función es creada para cargar el raster en el programa inicializado en iniciarPrograma()
    """
    pathTiff = "D:/Programacion/QGIS/Rasters/ImgsRaster/LC09_L1TP_009056_20250319_20250319_02_T1_B1.TIF"

    # Esto permite verificar el la ruta a nuestro documento funciona correctamente
    if not os.path.exists(pathTiff):
        print("No se ha encontrado el tiff")
        return

    #Cargando la capa en el proyecto
    try:
        rlayer: QgsRasterLayer = QgsRasterLayer(pathTiff, "B1_Landsat")
        if rlayer.isValid():
            QgsProject.instance().addMapLayer(rlayer)
            print("La capa se ha cargado con exito")
        else:
            print("El archivo seleccionado no es valido")
            return
    except Exception as ex:
        print(f"El error es este: {ex}")

def iniciarPrograma () -> None:

    QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.40.5/apps/qgis-ltr",True)
    qgis = QgsApplication ([],True)

    try:
        qgis.initQgis()
        print("El programa se ha iniciado corectamente")
        importarRaster()
    except Exception as ex:
        print(f"El error ocurrido es el siguiente: {ex}")
    finally:
        qgis.exitQgis()

if __name__ == "__main__":
    iniciarPrograma()