num = int(input('Ingresar un numero: '))

b_list = []
for i in range(num):
    b = input('Ingresar nombre: ')
    b_list.append(b)


for i in range(num):
    if i % 2 == 0:
        print(f"B({i})={b_list[i]}")
