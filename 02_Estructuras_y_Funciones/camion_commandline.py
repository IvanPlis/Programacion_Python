import csv
import sys

def costo_camion(dir):
    """
    Calcula el costo total de la mercaderia de un camion
    """

    costo_total = 0

    f = open(dir, 'rt', encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)

    for row in rows:
        try:
            costo_camion = int(row[1]) * float(row[2])
            costo_total = costo_total + costo_camion
            print(row)
        except ValueError:
            print(f'Precio de {row[0]} no encontrado en el archivo')

    costo_formateado = f'\nEl costo total es:{costo_total:>10}'
    return costo_formateado

if len(sys.argv) == 2:
    dir = sys.argv[1]
else:
    dir = '../Data/missing.csv'

costo_camion = costo_camion(dir)
print(costo_camion)