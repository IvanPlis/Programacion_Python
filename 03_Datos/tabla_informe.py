import csv
from pprint import pprint
import sys

def leer_camion(archivo):
    """
    Lee un csv con los datos de la mercaderia de un camion y retorna
    en una lista de dicts con los header como claves 
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


def leer_precios(archivo):
    """
    Lee un csv y retorna un dict con formato mercaderia['fruta'] = precio
    """

    precios = dict()

    with open(archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)

        for n_row, row in enumerate(rows):
            try:
                fruta = row[0]
                precio = float(row[1])
                precios[fruta] = precio

            except ValueError:
                print(f'Precio de {n_row+1} no encontrado en el archivo')

            except IndexError:
                print(f'Fila vacia en {n_row+1}')

    return precios


def hacer_informe(camion, precios):
    """ 
    Comprueba que la mercaderia del camion este en la lista de precios 
    y hace un balance con las que si estan. Retorna una tupla con la
    mercaderia y el balance.
    """

    informe = []

    for fruta in camion:
        nombre_fruta = fruta['nombre']
        ncajones = fruta['cajones']

        if nombre_fruta in precios:
            precio_compra = fruta['precio']
            precio_venta = precios[nombre_fruta]
            
            balance = precio_venta - precio_compra

            informe_fruta = (nombre_fruta, ncajones, precio_venta, balance)
            informe.append(informe_fruta)

    return informe


def imprimir_informe(informe):
    """
    Imprime el informa con un formato de tabla
    """
    
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    div = ('----------')

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{div:>10s} {div:>10s} {div:>10s} {div:>10s}')

    for nombre, cajones, precio, balance in informe:
        precio_signo = f'${precio:.2f}'
        print(f'{nombre:>10s} {cajones:>10d} {precio_signo:>10} {balance:>10.2f}')


if len(sys.argv) == 3:
    archivo_camion = sys.argv[1]
    archivo_precios = sys.argv[2]
else:
    archivo_camion = '../Data/camion.csv'
    archivo_precios = '../Data/precios.csv'


camion = leer_camion(archivo_camion)
precios = leer_precios(archivo_precios)
informe = hacer_informe(camion, precios)

imprimir_informe(informe)
