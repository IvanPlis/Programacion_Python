import csv
from pprint import pprint
import sys
from collections import Counter

def leer_parque(nombre_archivo, parque):
    """
    Abre el archivo indicado y devuelve una lista de dicts
    por cada arbol del parque elegido
    """

    lista_arboles = []

    with open (nombre_archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)
        header = next(rows)

        for n_row, row in enumerate(rows):
            if parque in row:
                try:
                    # Convierto los datos que necesito como int o float
                    arbol = dict(zip(header, row))
                    arbol['long'] = float(arbol['long'])
                    arbol['lat'] = float(arbol['lat'])
                    arbol['id_arbol'] = int(arbol['id_arbol'])
                    arbol['altura_tot'] = int(arbol['altura_tot']) 
                    arbol['diametro'] = int(arbol['diametro']) 
                    arbol['inclinacio'] = int(arbol['inclinacio'])
                    arbol['coord_x'] = float(arbol['coord_x']) 
                    arbol['coord_y'] = float(arbol['coord_y'])
                
                    lista_arboles.append(arbol)

                except ValueError:
                    print(f'Fila {n_row}: No se pudo interpretar: {row}')

                except IndexError:
                    print(f'Fila vacia en {n_row+1}')

    return lista_arboles


def informe(lista_arboles):

    headers = ('Longitud', 'Latitud', 'ID_Arbol', 'Altura', 'Diametro', 'Inclinacion',
               'ID Especie', 'Nombre Comp', 'Nombre Cie', 'Follaje', 'Parque', 'Ubicacion',
               'Familia', 'Genero', 'Origen', 'Coord X', 'Coord Y')
    
    for header in headers:
        if isinstance(header, str):
            print(f'{header:>20s}|', end='')
        elif isinstance(header, float):
            print(f'{header:>20f}|', end='')
        elif isinstance(header, int):
            print(f'{header:>20d}|', end='')
    print()
    div = '-' * 340
    print(div)

    for i, arbol in enumerate(lista_arboles):

        print(f'{arbol["long"]:>20f}|', end='')
        print(f'{arbol["lat"]:>20f}|', end='')
        print(f'{arbol["id_arbol"]:>20d}|', end='')
        print(f'{arbol["altura_tot"]:>20d}|', end='')
        print(f'{arbol["diametro"]:>20d}|', end='')
        print(f'{arbol["inclinacio"]:>20d}|', end='')
        print(f'{arbol["id_especie"]:>20s}|', end='')
        print(f'{arbol["nombre_com"]:>20s}|', end='')
        print(f'{arbol["nombre_cie"]:>20s}|', end='')
        print(f'{arbol["tipo_folla"]:>20s}|', end='')
        print(f'{arbol["espacio_ve"]:>20s}|', end='')
        print(f'{arbol["ubicacion"]:>20s}|', end='')
        print(f'{arbol["nombre_fam"]:>20s}|', end='')
        print(f'{arbol["nombre_gen"]:>20s}|', end='')
        print(f'{arbol["origen"]:>20s}|', end='')
        print(f'{arbol["coord_x"]:>20f}|', end='')
        print(f'{arbol["coord_y"]:>20f}|')
        print(div)


def mostrar_datos_altura(lista_arboles, especie):
    """
    Recibe un parque y una especie y muestra la altura maxima y el
    primedio de las alturas de arboles de dicha especie.
    """

    alturas = obtener_alturas(lista_arboles, especie)

    if alturas:

        max_altura = max(alturas)
        prom_altura = round(sum(alturas) / len(alturas), 2)
        print(f"Altura maxima {especie.upper():>12} {max_altura:>10}")
        print(f"Altura promedio {especie.upper():>10} {prom_altura:>10}")
    

def obtener_alturas(lista_arboles, especie):
    """
    Devuelve las alturas de los arboles de una especie en un parque
    """

    arboles_especie = get_arboles_especie(lista_arboles, especie)
    alturas = []
    print(arboles_especie)

    for arbol in arboles_especie:
        altura_arbol = arbol['altura_tot']
        alturas.append(altura_arbol)

    return alturas


def get_arboles_especie (lista_arboles, especie):
    """
    Recorre un parque y devuelve los arboles de una especien particular
    """

    arboles_especie = []

    for arbol in lista_arboles:
        if especie == arbol['nombre_com']:
            arboles_especie.append(arbol)

    if arboles_especie is None:
        print(f'{especie.upper()} no encontrado en parque {lista_arboles[0]["espacio_ve"].upper()}') 
    
    return arboles_especie


def get_especies(lista_arboles):
    """
    Toma una lista de árboles y retorna el conjunto de especies (la columna
    'nombre_com' del archivo) que figuran en la lista
    """

    especies = set()

    for arbol in lista_arboles:
        nombre_arbol = arbol['nombre_com']
        if nombre_arbol not in especies:
            especies.add(nombre_arbol)
    
    return especies



def contar_ejemplares(lista_arboles):
    """
    Devuelve un dict con especies como key y cantidad como value
    """

    total_ejemplares = Counter()

    for arbol in lista_arboles:
        nombre_arbol = arbol['nombre_com']
        total_ejemplares[nombre_arbol] += 1  

    return total_ejemplares


def ejemplares_mas_comunes(ejemplares, cant):
    mas_comunes = ejemplares.most_common(cant)
    pprint(mas_comunes)

# A partir de aca se utilizan las técnicas de comprension de listas aprendidas
# y se aprovecha el hecho de trabajar con objetos
def leer_arboles(nombre_archivo):
    """
    Lee el archivo indicado y devuelva una lista de diccionarios con la
    información de todos los árboles en el archivo.
    """

    with open(nombre_archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)
        header = next(rows)

        # Define los tipos de datos de cada columna para su conversion
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
        arboleda = []

        for n_row, row in enumerate(rows):
            try:
                # Crea el dict iterando para todos los headers y convirtiendo al type respectivo
                arbol = {name: func(val) for name, func, val in zip(header, types, row)}
                arboleda.append(arbol)
            except ValueError:
                print(f'Fila {n_row}: No se pudo interpretar: {row}')
            except IndexError:
                print(f'Fila vacia en {n_row + 1}')

    return arboleda


def obtener_alturas_2(arboleda, especie):
    """
    Recibe una lista de arboles y una especie, y devuelve todas las alturas
    de los arboles de dicha especie.
    """

    alturas = {arbol['id_arbol']: arbol['altura_tot'] for arbol in arboleda if especie == arbol['nombre_com']}
    return alturas


def obtener_medidas(arboleda, especie):
    alturas_diam = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if especie == arbol['nombre_com']]
    return alturas_diam


def medidas_de_especie(arboleda, especies): 
    medidas = {especie: obtener_medidas(arboleda, especie) for especie in especies}
    return medidas


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'


lista_arboles_1 = leer_parque(nombre_archivo, 'GENERAL PAZ')
"""
lista_arboles_2 = leer_parque(nombre_archivo, 'ANDES, LOS')
lista_arboles_3 =  leer_parque(nombre_archivo, 'CENTENARIO')

especies = get_especies(lista_arboles_1)


ejemplares_1 = contar_ejemplares(lista_arboles_1)
mostrar_datos_altura(lista_arboles_1, 'Jacarandá')

ejemplares_2 = contar_ejemplares(lista_arboles_2)
ejemplares_3 = contar_ejemplares(lista_arboles_3)

ejemplares_mas_comunes(ejemplares_1, 5)
ejemplares_mas_comunes(ejemplares_2, 5)
ejemplares_mas_comunes(ejemplares_3, 5)

mostrar_datos_altura(lista_arboles_1, 'Jacarandá')
"""


arboleda = leer_arboles(nombre_archivo)
"""
alturas = obtener_alturas_2(arboleda, 'Jacarandá')
print(alturas)

altura_diam = obtener_medidas(arboleda, 'Jacarandá')
print(altura_diam)
"""

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas_especie = medidas_de_especie(arboleda, especies)
print(medidas_especie)