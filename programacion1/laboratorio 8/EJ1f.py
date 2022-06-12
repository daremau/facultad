num = int(input('Ingresar un numero: '))

a_list = []
for i in range(num):
    a = input('Ingresar nombre: ')
    a_list.append(a)

for i in range(num):
    if i % 2 != 0:
        print(f"A({i}) = {a_list[i]}", end=", ")