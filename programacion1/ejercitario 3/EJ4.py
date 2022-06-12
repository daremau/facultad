n = int(input('Ingresar dimesion de los vectores: '))

vector = []
par = []
impar = []

for i in range(n):
    num = int(input('Ingresar un numero: '))
    vector.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

if par:
    print(f"Suma y promedio de pares: {sum(par)}, {sum(par) / len(par)}")
else:
    print('No se pudo calcular los pares')
if impar:
    print(f"Suma y promedio de impares: {sum(impar)}, {sum(impar) / len(impar)}")
else:
    print('No se pudo calcular los impares')
