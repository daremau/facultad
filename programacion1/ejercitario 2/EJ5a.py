menor = None
for i in range(100):
    num_x = int(input('Ingresar numero X: '))
    if menor is None:
        menor = num_x

    if menor > num_x:
        menor = num_x

    print(menor)


