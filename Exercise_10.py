# Pedir 10 numeros al usuario y mostrar cuantos de ellos han sido cero

# Algoritmo ContarNumeros_Para

contador = 0
positivos = 0
numero = 0

for contador in range(10):
    numero = int(input('Dame un numero: '))

    if numero > 0:
        positivos = positivos + 1
print('Has introducido ' + str(positivos) + ' numeros mayores de cero')
