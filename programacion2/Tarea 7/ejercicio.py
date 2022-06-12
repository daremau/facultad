from sympy import prime


N = input('Ingresar un numero de tres cifras: ')

decenas = ['', 'dieci', 'veinti', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
centenas = ['', 'Ciento', 'Doscientos', 'Trescientos', 'Cuatrocientos', 'Quinientos', 'Seiscientos', 'Setesientos', 'Ochocientos', 'Novecientos']
numeros = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
diez = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince']

if len(N) == 3:
    segundo = ''
    tercero = ''
    if int(N) == 100:
        primero = 'Cien'
    else:
        i = 0
        j = 0
        while i < 10 or j < 10:
            if int(N[0]) == j:
                primero = centenas[i]
            i += 1
            j += 1

    if 9 < int(N[1] + N[2]) < 16:
        i = 0
        j = 10
        while i < 5 or j < 16:
            if int(N[1] + N[2]) == j:
                segundo = diez[i]
            i += 1
            j += 1
    else:
        if int(N[2]) == 0:
            if int(N[1]) == 2:
                segundo = 'veinte'
            else:
                i = 0
                j = 0
                while i < 10 or j < 11:
                    if int(N[1]) == i:
                        segundo = decenas[i]
                    i += 1
                    j += 1
        else:
            i = 0
            j = 0
            while i < 10 or j < 11:
                if int(N[1]) == i:
                    segundo = decenas[i] + ' y '
                if int(N[2]) == i:
                    tercero = numeros[i] 
                i += 1
                j += 1

    print(primero, segundo + tercero)

else:
    print('El numero no es de tres cifras')