def invertir_lista(lista):
    invertida = []
    len_lista = len(lista) - 1
    for e in lista: # Recorro la lista
        invertida.append(lista[len_lista]) #agrego el elemento e al principio de la lista invertida
        len_lista -= 1
    return invertida

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

inv_1 = invertir_lista(lista_1)
inv_2 = invertir_lista(lista_2)

print(inv_1)
print(inv_2)