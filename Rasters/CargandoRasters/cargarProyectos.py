from qgis.core import QgsApplication, QgsProject, QgsRasterLayer

"""
Este código es un código prueba inicial para el correcto uso de PyQGIS por fuera del programa QGIS, principalmente
es para aprendizaje y entendimiento de las funcionalidades
"""

def iniciarPrograma () -> None:
    """
    setPrefixPath le permite saber a la aplicación donde se va a encontrar el qgis del cual se quiere hacer uso
    """
    QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.40.5/apps/qgis-ltr",True)

    """
    qgis es necesario para indicarle al programa que clase de programa se va a realizar si una automatización  sin interfaz
    gráfica; en cuyo caso donde se encuentra True, colocar False; si no va a ser así y va a manipular objetos que quiere
    visualizar colocar True
    """
    qgis = QgsApplication([],True)

    try:
        qgis.initQgis()
        print("Iniciado Correctamente")
    except Exception as e:
        print(f"Ha ocurrido el siguiente error: {e}")
    finally:
        qgis.exitQgis()

iniciarPrograma()

