import rasterio
import numpy as np

ruta = "D:/Programacion/QGIS/Rasters/ImgsRaster/LC09_L1TP_009056_20250319_20250319_02_T1_B1.TIF"

with rasterio.open(ruta) as src:
    data = src.read(1)  # Banda 1
    nodata = src.nodata

    print(f"Tipo de datos: {data.dtype}")
    print(f"Valor NoData declarado: {nodata}")
    print(f"Valor mínimo (incluyendo NoData): {data.min()}")
    print(f"Valor máximo (incluyendo NoData): {data.max()}")

    if nodata is not None:
        data_masked = np.ma.masked_equal(data, nodata)
        print(f"Valor mínimo real (sin NoData): {data_masked.min()}")
        print(f"Valor máximo real (sin NoData): {data_masked.max()}")