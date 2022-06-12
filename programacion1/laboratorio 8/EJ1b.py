num = int(input('Ingresar un numero: '))

b_list = []
for i in range(num):
    b = input('Ingresar nombre: ')
    b_list.append(b)

for i in range(num):
    print(f"B({num - (i + 1)}) = {b_list[num - (i + 1)]}", end=", ")

