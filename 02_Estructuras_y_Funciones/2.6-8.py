#%%
def saludar(nombre):
        'Saluda a alguien'
        print('Hola', nombre)

saludar('ivan')

help(saludar)

#%%
"""
2.7
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función
buscar_precio(fruta) que busque en archivo ../Data/precios.csv el 
precio de determinada fruta (o verdura) y lo imprima en pantalla. 
Si la fruta no figura en el listado de precios, debe imprimir un 
mensaje que lo indique.
"""

dir = '../Data/precios.csv'
costo_total = 0

def buscar_precio(fruta):
     """Busca en el csv si existe una fruta y su precio. Si no la encuentra devuelve error."""

     fruta.lower()
     fruta_encontrada = False

     with open(dir, 'rt', encoding='utf8') as f:
        for line in f:
            row = line.lower().split(',')
            row[-1] = row[-1].strip()

            if (row[0] == fruta):
                precio_fruta = float(row[1])
                precio_formateado = f'\nEl precio de la {fruta} es:{precio_fruta:>8}'
                fruta_encontrada = True
                break

     if fruta_encontrada:
        print(precio_formateado)
     else:
        print(f"No se encontro la fruta {fruta}")
            
buscar_precio('naranja') 
buscar_precio('pera')

# %%
"""
2.8
Manejo de excepciones
"""

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

edad = preguntar_edad('ivan')


# %%
# mediante datos ingresado por el usuario
for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')


# %%
"""
Modificá el programa costo_camion.py para que atrape la excepción con un bloque try - except,
imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.
"""

def costo_camion(dir):
    """
    Calcula el costo total de la mercaderia de un camion"""

    costo_total = 0

    with open(dir, 'rt', encoding='utf-8') as f:
        
        headers = next(f).split(',')
        headers[-1] = headers[-1].strip()   # elimino el salto de linea
        print(headers)

        for line in f:
            row = line.split(',')
            row[-1] = row[-1].strip()

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
