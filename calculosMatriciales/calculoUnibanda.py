import xarray
from qgis.core import QgsApplication, QgsProject, QgsRasterLayer, QgsRasterDataProvider
from pathlib import Path
from osgeo import gdal
import re
import xarray as xr
import rasterio
import numpy as np
import pandas as pd


def calUnibanda(bandas: list) -> None:

    new_nodata = -9999
    gdal.UseExceptions()

    # Rutas de archivos
    ruta_entrada = Path.cwd().parent / 'Rasters' / 'ImgsRaster' / 'LC09_L1TP_009056_20250319_20250319_02_T1_B1.TIF'
    ruta_salida = Path.cwd().parent / 'Rasters' / 'ImgsRaster' / 'LC09_L1TP_009056_20250319_20250319_02_T1_B1_EDITADO.TIF'

    # Verificar metadatos originales
    with rasterio.open(ruta_entrada) as src:
        print("\nMetadatos originales:")
        print(f"Tipo de dato: {src.dtypes[0]}")
        print(f"NoData actual: {src.nodata}")

    # Configurar opciones de traducción
    opciones = gdal.TranslateOptions(
        format='GTiff',
        outputType=gdal.GDT_Float32,
        noData=new_nodata,
        creationOptions=['COMPRESS=DEFLATE']  # Compresión opcional
    )

    # Ejecutar traducción
    try:
        gdal.Translate(
            destName=str(ruta_salida),
            srcDS=str(ruta_entrada),
            options=opciones
        )

        # Verificar resultados
        with rasterio.open(ruta_salida) as src:
            print("\nMetadatos procesados:")
            print(f"Tipo de dato: {src.dtypes[0]}")
            print(f"Nuevo NoData: {src.nodata}")

    except Exception as e:
        print(f"\nError en GDAL Translate: {str(e)}")

    with rasterio.open(ruta_salida) as src:
        img = src.read(1)

    data = xr.DataArray(img)
    datMasked = np.ma.masked_equal(data,src.nodata)
    print(datMasked.min(), datMasked.max(), np.mean(datMasked))

def uploadingRaster() -> list:
    # Cargando el proyecto de QGIS
    project = QgsProject().instance()
    root = project.layerTreeRoot()

    rutaPadre = Path.cwd().parent
    rutaTif = rutaPadre / 'Rasters' / 'ImgsRaster'

    # Verificando si la carpeta hacia los archivos existe
    if not rutaTif.exists():
        print("La ruta de archivos no existe")
        return []

    # Función para extraer el número de banda del nombre del archivo
    def obtener_num_banda(nombre):
        match = re.search(r'_B(\d+)', nombre.upper())
        return int(match.group(1)) if match else float('inf')

    # Cargando todos los rasters que existen en la carpeta
    tiposDato = {'tif', 'tiff', 'jpg', 'jp2', 'jpeg'}
    archivos = sorted(
        (str(archivo) for archivo in rutaTif.rglob('*')
         if archivo.is_file() and archivo.suffix.lower()[1:] in tiposDato),
        key=lambda x: obtener_num_banda(Path(x).name)
    )

    layersCargados = []
    rts = root.addGroup('Rasters')

    # Cargando los rasters
    for i, archivo in enumerate(archivos, start=1):
        rlayer = QgsRasterLayer(str(archivo), f"Banda{i}")
        if not rlayer.isValid():
            raise Exception(f'La imagen {archivo} no es válida')

        project.addMapLayer(rlayer)
        layersCargados.append(rlayer)

        nodo = root.findLayer(rlayer.id())
        rts.addChildNode(nodo.clone())
        root.removeChildNode(nodo)

    return layersCargados

def iniciandoQgis() -> None:

    QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.40.5/apps/qgis-ltr", True)
    qgis = QgsApplication([], True)

    try:
        qgis.initQgis()
        bandas : list = uploadingRaster()
        calUnibanda(bandas)

    except Exception as ex:
        print(f"Ocurrio el siguiente error: {ex}")
        return

    finally:
        qgis.exitQgis()

if __name__ == "__main__":
    iniciandoQgis()
