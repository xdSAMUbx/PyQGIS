from pathlib import Path
import pandas as pd
from qgis.core import (
    QgsApplication,
    QgsRasterLayer,
    QgsProject
)

def usigRasters(grupo, layers) -> None:
    # Este codigo es principalmente el utilizado para el uso de las capas raster cargadas anteriormente en loadingLayers

    # Creando carpeta donde se guardaran los datos obtenidos de las capas
    carpetaPadre = Path.cwd().parent
    carpetaDatos = carpetaPadre / "datosRasters"
    carpetaDatos.mkdir(parents=True, exist_ok=True)

    # Obtener dimensiones del raster
    dim = [[layer.name(),layer.width(), layer.height()] for layer in layers if layer.isValid()]
    df_dim =  pd.DataFrame(dim, columns=["Bandas","Ancho (px)","Alto(px)"])

    # Guardando en excel
    salidaExcel = carpetaDatos / 'dimRasters.xlsx'
    df_dim.to_excel(salidaExcel, index=False)
    print(f'El excel con las dimensiones se ha guardado en: {salidaExcel}')

def loadingLayers(): # No se específica que devuelve la función para evitar futuros errores

    """
    En este codigo se buscará cargar múltiples documentos raster con el fin de automatizar este proceso para el proyecto.
    Todas las funciones aquí utilizadas serán complementarias para el futuro desarrollo y entendimiento de cualquier Plugin
    """

    proyecto = QgsProject.instance()
    rutaCarpeta = Path('D:/Programacion/QGIS/Rasters/ImgsRaster')

    if not rutaCarpeta.exists(): #Verifica que la carpeta exista, si exite no pasa nada, si no, se acaba
        print("La dirección de las imagenes no existe")
        return

    archivos : list = [] #Se crea la lista de archivos con la finalidad de que si no existe nada permita culminar el código

    # Esta sección del código permite verificar si el usuario esta cargando correctamente los archivos que posteriormente se van a manejar
    try:
        archivos : list = [doc for doc in rutaCarpeta.iterdir() if doc.suffix.lower() in ['.tif','.tiff']] #Permite unir el archivo raster con la ruta de la carpeta para futuros usos
        if not archivos:
            print("No se han encontrado archivos .tiff")
            return
    except Exception as ex:
        print(f"Ocurrio el siguiente error: {ex}")
        return

    # Creando un grupo para todos los rasters cargados
    layersCargados = []
    root = proyecto.layerTreeRoot()
    rts = root.addGroup('Rasters')

    # Cargando los rasters al proyecto iniciado
    for i, archivo in enumerate(archivos, start=1):

        try:
            #Obtiene el nombre de la capa basado en el archivo
            nameLayer = archivo.stem
            capasExistentes = {lyr.source(): lyr for lyr in proyecto.mapLayers().values()}
            if str(archivo) in capasExistentes:
                print(f'La imagen ya esta cargada')
                continue

            # Crear y validar capa
            rlayer = QgsRasterLayer(str(archivo), nameLayer)
            if not rlayer.isValid():
                raise Exception(f"Archivo inválido: {nameLayer}")

            # Añadir al proyecto y grupo
            proyecto.addMapLayer(rlayer)
            layersCargados.append(rlayer)

            # Mover al grupo
            nodo = root.findLayer(rlayer.id())
            rts.addChildNode(nodo.clone())
            root.removeChildNode(nodo)

        except Exception as ex:
            print(f"Error procesando {archivo.name}: {ex}")

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
        return

    finally:
        qgis.exitQgis()

if __name__ == "__main__":
    startingProject()

