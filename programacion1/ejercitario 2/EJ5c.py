menor = None
while True:
    num = int(input('Ingresar un numero: '))

    if menor is None:
        menor = num

    if menor > num:
        menor = num

    if num == -9999:
        break
