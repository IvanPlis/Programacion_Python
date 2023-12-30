def propagar(lista_fosforos):
    """
    Recibe una lista de fosforos y propaga el fuego de los fosoforos
    encendidos a sus vecinos (izq y der) si estos estan apagados.
    Devuelve una lista con los fosforos que se encendieron.

    1: encendido
    0: apagado
    -1: consumido (no se pueden encender)
    """

    # Para no modificar la lista original
    propagado = copiar_lista(lista_fosforos)
    # Agrego un elemento mas temporalmente para evitar el index out of range
    propagado.append(0)

    # Recorro la lista de fosforos
    for i, fosforo in enumerate(propagado): 
        # Verifico si esta encendido
        if fosforo == 1:
           
            # Propaga el fuego al fosforo de la derecha
            j = i + 1 
            while propagado[j] == 0 and j < len(propagado) - 1:
                propagado[j] = 1
                j += 1

            # Propaga al fuego al fosforo de la izquierda
            j = i - 1
            while propagado[j] == 0 and j >= 0:
                propagado[j] = 1
                j -= 1

    # Elimino el elemento extra temporal
    propagado.pop(len(propagado)-1)

    return propagado


def copiar_lista(lista_original):
    copia_lista = []
    for elemento in lista_original:
        copia_lista.append(elemento)
    return copia_lista


print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0, 1, 0, 0]))