# Pedir contrasena 3 intentos maximo usando repetir
clave = 0
intentos = 0

while(intentos < 3):
    intentos = intentos + 1
    clave = int(input('Dame la clave: '))
    if clave == 352 or clave == 259 or clave == 569:
        print('Clave Correcta')
        intentos = 3
    else: 
        print('Demasiados intentos')
        


    
    