"""
2.1

Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de
cajones cargados en el camión, y un precio de compra por cada cajón de ese
grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea
las líneas, y calcule el precio pagado por los cajones cargados en el camión.
"""

dir = '../Data/camion.csv'
costo_total = 0

with open(dir, 'rt', encoding='utf8') as f:
    headers = next(f).split(',')
    headers[-1] = headers[-1].strip()   # elimino el salto de linea
    print(headers, end='')

    for line in f:
        row = line.split(',')
        row[-1] = row[-1].strip()
        costo_camion = int(row[1]) * float(row[2])
        costo_total = costo_total + costo_camion
        print(row, end='')

costo_formateado = f'\nEl costo total es:{costo_total:>10}'
print(costo_formateado)

        
