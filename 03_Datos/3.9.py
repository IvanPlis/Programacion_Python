"""
Modificar leer_camion .py para que entienda que la columna tiene el precio
por su encabezado y no por su posición dentro del archivo.
"""

import csv
import pprint
import sys

def leer_camion(archivo):
    """
    Lee un csv y guarda una lista (camion) de dicts (mercaderias) con los
    headers como keys
    """

    camion = []

    with open(archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)
        header = next(rows)

        for n_row, row in enumerate(rows):
            try:
                registro = dict(zip(header, row))
                registro['cajones'] = int(registro['cajones'])
                registro['precio'] = float(registro['precio'])
                camion.append(registro)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')

    return camion


def print_camion(camion):
    for registro in camion:
        print(registro)


def costo_camion(camion):
    costo_total = 0
    for registro in camion:
        n_cajas = registro['cajones']
        precio = registro['precio']
        costo_total += n_cajas * precio

    print(f'El costo total del camion es: {costo_total:>10}')


if len(sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = '../Data/camion.csv'

camion = leer_camion(archivo)
print_camion(camion)
costo_camion(camion)