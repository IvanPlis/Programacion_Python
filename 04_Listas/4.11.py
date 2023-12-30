import csv
import sys

def leer_camion(nombre_archivo):
    """
    Recibe un csv de la mercaderia de un camion y devuelve las tablas
    consultadas como una lista de dicts
    """
    with open(nombre_archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)
        headers = next(rows)

        # Guardo las columnas que quiero consultar
        select = ['nombre', 'cajones', 'precio']

        # Indices de las columnas seleccionadas en el archivo
        indices = [headers.index(ncolumna) for ncolumna in select]

        # Recorre los nombres de la columna y sus indicies para guardar su contenido
        # como dict nombre: {datos}
        # Repite para cada linea del CSV
        record = [[{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]]
    
    return record


if len(sys.argv) == 3:
    archivo_camion = sys.argv[1]
    archivo_precios = sys.argv[2]
else:
    archivo_camion = '../Data/camion.csv'
    archivo_precios = '../Data/precios.csv'

camion = leer_camion(archivo_camion)
print(camion)