"""
USANDO EL DEBUGGER
La primera vez que se elimina un elemento de la lista es cuando
se utiliza el metodo pop. Las listas se pasa por referencia, habría
que copiar la lista original en una varibale y trabajar sobre ella.
"""

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')