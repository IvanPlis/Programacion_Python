"""
2.3

El archivo ../Data/precios.csv contiene una serie de líneas con precios de 
venta de cajones en el mercado al que va el camión. 
Escribí un código que abra el archivo ../Data/precios.csv, busque el precio 
de la naranja y lo imprima en pantalla."""

dir = '../Data/precios.csv'
costo_total = 0

with open(dir, 'rt', encoding='utf8') as f:
    for line in f:
        row = line.lower().split(',')
        row[-1] = row[-1].strip()
        if (row[0] == 'naranja'):
            precio_naranja = float(row[1])
            precio_formateado = f'\nEl precio de la naranja es:{precio_naranja:>8}'
            print(precio_formateado)
        else:
            pass