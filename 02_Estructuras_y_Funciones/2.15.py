"""
2.15
En este archivo, definí una función leer_camion(nombre_archivo) que abre un 
archivo con el contenido de un camión, lo lee y devuelve la información como
una lista de tuplas. Para hacerlo vas a tener que hacer algunas 
modificaciones menores al código de arriba.
"""

import csv
import sys

def leer_camion(nombre_archivo):
    """
    Calcula el costo total de la mercaderia de un camion
    """
    
    camion = []
    f = open(nombre_archivo, 'rt', encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            cargamento = (row[0], int(row[1]), float(row[2]))
            camion.append(cargamento)
        except ValueError:
            print(f'Precio de {row[0]} no encontrado en el archivo')

    return camion


def precio_camion(camion):
    "Calcula el costo total de la mercaderia del camion. No contempla cajones sin precio"

    total = 0.0
    for cargamento in camion:
        total += cargamento[1] * cargamento[2]

    costo_formateado = f'\nEl costo total es:{total:>10}'
    print(costo_formateado)   


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/missing.csv'

camion = leer_camion(nombre_archivo)
precio_camion(camion)