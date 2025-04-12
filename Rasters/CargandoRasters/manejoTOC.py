import os
import pandas as pd
from qgis.PyQt.QtGui import QColor
from qgis.core import (
    QgsApplication,
    QgsRasterLayer,
    QgsProject,
    QgsPointXY,
    QgsRaster,
    QgsRasterShader,
    QgsColorRampShader,
    QgsSingleBandPseudoColorRenderer,
    QgsSingleBandColorDataRenderer,
    QgsSingleBandGrayRenderer
)

def usigRasters(grupo, layers) -> None:
    # Este codigo es principalmente el utilizado para el uso de las capas raster cargadas anteriormente en loadingLayers

    # Creando carpeta donde se guardaran los datos obtenidos de las capas
    os.makedirs('datosRasters',exist_ok=True)

    # Obtener dimensiones del raster
    dim = [(layer.width(), layer.height()) for layer in layers if layer.isValid()]
    df_dim =  pd.DataFrame(dim, columns=["Ancho (px)","Alto(px)"])

    # Guardando en excel
    salidaExcel = os.path.join(os.getcwd(), 'datosRasters', 'dimRasters.xlsx')
    df_dim.to_excel(salidaExcel, index=False)
    print(f'El excel con las dimensiones se ha guardado en: {salidaExcel}')

def loadingLayers(): # No se específica que devuelve la función para evitar futuros errores

    """
    En este codigo se buscará cargar múltiples documentos raster con el fin de automatizar este proceso para el proyecto.
    Todas las funciones aquí utilizadas serán complementarias para el futuro desarrollo y entendimiento de cualquier Plugin
    """

    proyecto = QgsProject.instance()
    if not os.path.exists('D:/Programacion/QGIS/Rasters/ImgsRaster'): #Verifica que la carpeta exista, si exite no pasa nada, si no, se acaba
        print("La dirección de la carpeta no existe")
        return

    archivos : list = [] #Se crea la lista de archivos con la finalidad de que si no existe nada permita culminar el código

    # Esta sección del código permite verificar si el usuario esta cargando correctamente los archivos que posteriormente se van a manejar
    try:
        rutaCarpeta : str = 'D:/Programacion/QGIS/Rasters/ImgsRaster'
        archivos : list = [os.path.join(rutaCarpeta,doc) for doc in os.listdir(rutaCarpeta) if doc.lower().endswith(('.tif','.tiff'))] #Permite unir el archivo raster con la ruta de la carpeta para futuros usos
        if not archivos:
            print("No se han encontrado archivos .tiff")
            return
    except Exception as ex:
        print(f"Ocurrio el siguiente error: {ex}")

    # Creando un grupo para todos los rasters cargados
    layersCargados = []
    root = proyecto.layerTreeRoot()
    rts = root.addGroup('Rasters')

    # Cargando los rasters al proyecto iniciado
    for i, archivo in enumerate(archivos, start=1):
        rlayer : QgsRasterLayer = QgsRasterLayer(archivo, f"Banda{i}")
        if rlayer.isValid():
            proyecto.addMapLayer(rlayer)
            layersCargados.append(rlayer)
            #Añadiendo el raster a la carpeta Rasters
            nodo = root.findLayer(rlayer.id())
            rts.addChildNode(nodo.clone())
            root.removeChildNode(nodo)
        else:
            print(f"El archivo {archivo} no es valido")

    return rts, layersCargados

def startingProject () -> None:

    """
    Lo escrito en esta sección del código se ve un poco más en detalle en cargarCapas.py, cualquier profundización
    puede llevarse acabo en la página oficial en la documentación de QGIS
    """

    QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.40.5/apps/qgis-ltr", True)
    qgis = QgsApplication ([],True)

    try:
        qgis.initQgis()
        grupo,layers = loadingLayers()
        usigRasters(grupo, layers)

    except Exception as ex:
        print(f"Ocurrio el siguiente error: {ex}")
    finally:
        qgis.exitQgis()

if __name__ == "__main__":
    startingProject()

