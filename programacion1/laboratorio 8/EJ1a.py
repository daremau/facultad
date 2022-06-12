num = int(input('Ingresar un numero: '))

a_list = []
for i in range(num):
    a = input('Ingresar nombre: ')
    a_list.append(a)

for i in range(num):
    print(f"A({i + 1}) = {a_list[i]}", end=", ")