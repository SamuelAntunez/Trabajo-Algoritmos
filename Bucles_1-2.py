#algoritmo DIA_PARA contador

contador = 0
d = int(input('introduce un numero del 1 al 7: '))
for contador in range(1, 8):
    if contador == d:
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