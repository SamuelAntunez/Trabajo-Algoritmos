# algoritmo que muestra nombre del día

#algoritmo DIA_CASO

d = 0

d = int(input('Introduce un numero del 1 al 7: '))

if d >= 1 and d <= 7:
        if d == 1:
            print('Lunes')
        elif d == 2:
            print('martes')
        elif d == 3:
            print('miercoles')
        elif d == 4:
            print('jueves')
        elif d == 5:
            print('viernes')
        elif d == 6:
            print('sabado')
        elif d == 7:
            print('domingo')

else:
    print('el valor no es valido')