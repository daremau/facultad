lista = []
N = int(input("Ingrese el numero de elementos de la lista: "))
for i in range(N):
    lista.append(int(input("Ingrese un numero: ")))

for elemento in lista:
    if elemento == 0:
        lista.remove(elemento)
        lista.append(elemento)

print(lista)