lista = []
N = int(input("Ingrese el numero de elementos de la lista: "))

for i in range(N):
    lista.append(int(input("Ingrese un numero: ")))

ultimo = lista[-1]
lista.remove(ultimo)
lista.insert(0, ultimo)

print(lista)