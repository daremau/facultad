num = int(input('Ingresar un numero: '))

a_list = []
for i in range(num):
    a = input('Ingresar nombre: ')
    a_list.append(a)

for i in range(num):
    print(f"A({num - i}) = {a_list[num - (i + 1)]}", end=", ")
