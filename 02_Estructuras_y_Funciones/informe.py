"""
2.18
Supongo camion.csv costos del proveedor
precios.csv precio de venta al descargar
Calcular costo, recaudacion y margen de ganancia
"""

import csv
import sys


def leer_precios(nombre_archivo):
    """Abre el csv y lo guarda en un dict"""

    camion = dict()
    f = open(nombre_archivo, 'rt', encoding='utf-8')
    headers = next(f)
    rows = csv.reader(f)

    for row in rows:
        try:
            camion[row[0]] = float(row[-1])

        except ValueError:
            print(f'Precio de {row[0]} no encontrado en el archivo')
            
        except IndexError:
            print('El archivo contiene lineas vacias')

    return camion


def calcular_total(camion):
    """Calcula la suma de todos los precios unitarios de mercaderia"""

    total = 0.0
    for precio_fruta in camion.values():
        total += precio_fruta
    
    total = round(total, 2)
    costo_formateado = f'\nEl costo total es:{total:>10}'
    print(costo_formateado)

    return total   


def calcular_ganancia(ventas, costo):
    ganancia = ventas - costo
    ganancia = round(ganancia, 2)
    ganancia_formateada = f'\nLa ganancia es:{ganancia:>10}'
    print(ganancia_formateada)


if len(sys.argv) == 3:
    archivo_costos = sys.argv[1]
    archivo_precios = sys.argv[2]
else:
    archivo_costos = '../Data/camion.csv'
    archivo_precios = '../Data/precios.csv'


costos = leer_precios(archivo_costos)
precios = leer_precios(archivo_precios)

total_costos = calcular_total(costos)
total_precios = calcular_total(precios)

calcular_ganancia(total_precios, total_costos)