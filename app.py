import os
import data_clean
import pandas as pd


"""
Momento 3 -  Fecha límite enero 22 de enero.
Construir una aplicación de análisis de datos en Python. 
Este tomará datos de la api desarrollada en Spring Boot
para hacer analisis de datos sobre el restaurante
En mi caso usaré las puntuaciones y platillos para crear graficas
de platillos mejor puntuados contra los peores.

"""


def limpiar_consola():
    """
    Limpia la consola se considera una buena práctica por eso la estoy
    creando aquí como una adición de parte de mi curso de Platzi
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
