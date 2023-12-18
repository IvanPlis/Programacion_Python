"""
Escribir un programa que reciba una lista y un elemento, y devuelva la ultima
aparicion de ese elemento
"""

def buscar_u_elemento(lista, elemento):
    index = -1
    for i, elem in enumerate(lista):
        if elem == elemento:
            index = i
    return index


def buscar_n_elemento(lista, elemento):
    acum = 0
    for elem in lista:
        if elem == elemento:
            acum += 1
    return acum


def maximo(lista):
    max = lista[0]
    for elem in lista:
        if elem > max:
            max = elem
    return max
        

lista = [1,2,3,2,8,3,4]

num = 2
index = buscar_u_elemento(lista, num)
acum = buscar_n_elemento (lista, num)
print(f'El {num} aparece un total de {acum} veces y por ultima vez en la posicion {index}')

num = 5
acum = buscar_n_elemento (lista, num)
index = buscar_u_elemento(lista, num)
print(f'El {num} aparece un total de {acum} veces y por ultima vez en la posicion {index}')

max = maximo(lista)
print(max)

lista_2 = [-5, -4]
max = maximo(lista_2)
print(max)