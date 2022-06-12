import random as r

def tirar_dado():
    dado1 = r.randint(1, 6)
    dado2 = r.randint(1, 6)
    dado3 = r.randint(1, 6)
    suma_de_dados = dado1 + dado2 + dado3
    return suma_de_dados


def ordenar(arr):
    for i in range(len(arr)):
        for j in range(i + 1):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def busqueda(arr, objetivo):
    accu = 0
    for i in arr:
        if i == objetivo:
            accu += 1
    return accu

valores = []
frecuencias = []
N = int(input("Elegir cuantas veces se deben tirar los dados: "))

i = 0
while i < N:
    valores.append(tirar_dado())
    i += 1

ordenar(valores)

for i in valores:
    frec = busqueda(valores, i)
    frecuencias.append(frec)
    if frec > 1:
        valores.remove(i)

for i in range(len(frecuencias)):
    for j in range(i + 1):
        if frecuencias[i] > frecuencias[j]:
            valores[j], valores[i] = valores[i], valores[j]
            frecuencias[j], frecuencias[i] = frecuencias[i], frecuencias[j]

print("Valores      Frecuencia")
for i in range(len(valores)):
    print(valores[i], "           ", frecuencias[i])