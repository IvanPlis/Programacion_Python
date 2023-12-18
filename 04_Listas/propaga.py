def propagar(lista_fosforos):

    propagado = copiar_lista(lista_fosforos)
    propagado.append(0)

    for i, fosforo in enumerate(propagado):

        if fosforo == 1:
            j = i + 1
            while propagado[j] == 0 and j < len(propagado) - 1:
                propagado[j] = 1
                j += 1

            j = i - 1
            while propagado[j] == 0 and j >= 0:
                propagado[j] = 1
                j -= 1

    propagado.pop(len(propagado)-1)
    return propagado


def copiar_lista(lista_original):
    copia_lista = []
    for elemento in lista_original:
        copia_lista.append(elemento)
    return copia_lista


print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0, 1, 0, 0]))