"""
2.16
Ahora diccionario en vez de lista de tuplas
"""

import csv
import sys

def leer_camion(nombre_archivo):
    """
    Calcula el costo total de la mercaderia de un camion y devuele un dict
    donde la clave es la mercaderia y los valores precio x u y cantidad
    """
    
    camion = []
    f = open(nombre_archivo, 'rt', encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            mercaderia = dict()
            mercaderia['fruta'] = row[0]
            mercaderia['cajones'] = int(row[1])
            mercaderia['precio'] = float(row[2])
            camion.append(mercaderia)
            print(mercaderia)
        except ValueError:
            print(f'Precio de {row[0]} no encontrado en el archivo')

    return camion


def precio_camion(camion):
    """Calcula el costo total de la mercaderia del camion. No contempla
    cajones sin precio"""

    total = 0.0
    for mercaderia in camion:
        print(mercaderia['cajones'], mercaderia['precio'])
        total += mercaderia['cajones'] * mercaderia['precio']

    costo_formateado = f'\nEl costo total es:{total:>10}'
    print(costo_formateado)   


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/missing.csv'

camion = leer_camion(nombre_archivo)
precio_camion(camion)