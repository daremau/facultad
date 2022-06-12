import random

N = int(input('Ingresar cuantas veces hay extraer bolillas del bolillero: '))

lista_bolillas = []
digito = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(N):
    bolilla = random.randint(1000, 9999)
    lista_bolillas.append(str(bolilla))

for i in range(len(lista_bolillas)):
    for j in range(len(lista_bolillas[i])):
        if lista_bolillas[i][j] == '0':
            cantidad[0] += 1
        elif lista_bolillas[i][j] == '1':
            cantidad[1] += 1
        elif lista_bolillas[i][j] == '2':
            cantidad[2] += 1
        elif lista_bolillas[i][j] == '3':
            cantidad[3] += 1
        elif lista_bolillas[i][j] == '4':
            cantidad[4] += 1
        elif lista_bolillas[i][j] == '5':
            cantidad[5] += 1
        elif lista_bolillas[i][j] == '6':
            cantidad[6] += 1
        elif lista_bolillas[i][j] == '7':
            cantidad[7] += 1
        elif lista_bolillas[i][j] == '8':
            cantidad[8] += 1
        elif lista_bolillas[i][j] == '9':
            cantidad[9] += 1

for i in range(10):
    for j in range(i + 1, 10):
        if cantidad[j] < cantidad[i]:
            cantidad[j], cantidad[i] = cantidad[i], cantidad[j]
            digito[j], digito[i] = digito[i], digito[j]

print('DIGITO         CANTIDAD')
for i in range(10):
    print(f"  {digito[i]}                {cantidad[i]}")