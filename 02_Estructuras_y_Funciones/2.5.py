numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
    except KeyboardInterrupt:
        print('Programa interrumpido, saliendo...')
print(f'Ingresaste {n}.')