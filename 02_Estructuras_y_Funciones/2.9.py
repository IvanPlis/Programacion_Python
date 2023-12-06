#%%
"""
Veo como el modudlo csv me hace toda la conversion a lista de una
"""

import csv

dir = '../Data/camion.csv'
f = open(dir, 'rt', encoding='utf-8')

rows = csv.reader(f)
headers = next(rows)
print(headers)

for row in rows:
    print(row)


# %%
"""
2.9
Modificá tu programa costo_camion.py para que use el módulo csv para leer los
archivos CSV y probalo en un par de los ejemplos anteriores.
"""

import csv

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
    print(costo_formateado)

dir = '../Data/missing.csv'
costo_camion(dir)

# %%
