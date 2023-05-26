# Pedir dos valores y en caso de que no sean iguales indicar cual es el mayor

# Algoritmo Leer

x = 0
y = 0

print('Dame dos numeros')
x = int(input('x: '))
y = int(input('y: '))
if x == y:
    print('Son iguales')
elif x > y:
    print('x es mayor')
else: 
    print('y es mayor')