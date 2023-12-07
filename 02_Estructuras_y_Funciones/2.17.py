"""
2.17
Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto
de precios como éste arme un diccionario donde las claves sean los nombres 
de frutas y verduras, y los valores sean los precios por cajón.
"""

import csv
import sys
from pprint import pprint

def leer_precios(nombre_archivo):
    """
    Arma un dict mercaderia['fruta'] = precio
    """

    mercaderia = dict()
    f = open(nombre_archivo, 'rt', encoding='utf-8')
    headers = next(f)
    rows = csv.reader(f)

    for row in rows:
        try:
            mercaderia[row[0]] = float(row[1])

        except ValueError:
            print(f'Precio de {row[0]} no encontrado en el archivo')
            
        except IndexError:
            print('El archivo contiene lineas vacias')

    pprint(mercaderia)
        

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/precios.csv'

leer_precios(nombre_archivo)