num = int(input('Ingresar numero N: '))

menor = None
for i in range(num):
    num_x = int(input('Ingresar otro numero: '))
    if menor is None:
        menor = num_x

    if menor > num_x:
        menor = num_x
