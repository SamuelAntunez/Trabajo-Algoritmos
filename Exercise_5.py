# Leer tres numeros y deducir si se han introducido en orden creciente

# Algoritmo N32

a = 0
b = 0
c = 0

print('dame tres numeros ')
a = int(input())
b = int(input())
c = int(input())

if a < b and b < c:
    print('en orden creciente')
elif a > b and b > c: 
    print('en orden decreciente')
else: 
    print('orden aleatorio')
