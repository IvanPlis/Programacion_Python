frase = 'Los hermanos sean unidos porque ésa es la ley primera'
palabras = frase.split()
sufijo_inclusivo = 'es'

for i, palabra in enumerate(palabras):
    if palabra.endswith('os'):
        palabra_inclusiva = palabra[:-2] + sufijo_inclusivo
        palabras[i] = palabra_inclusiva
        
frase_t = ' '.join(palabras)
print(frase_t)