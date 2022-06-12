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
        impar.append((num))

if not par:
    par = [0]
elif not impar:
    impar = [0]

print(f"Suma y promedio de pares: {sum(par)}, {sum(par) / len(par)}\n"
      f"Suma y promedio de impares: {sum(impar)}, {sum(impar) / len(impar)}")
