num = int(input('Ingresar un numero: '))

a_list = []
b_list = []
for i in range(num):
    a = input('Ingresar nombre para A: ')
    a_list.append(a)
    b = input('Ingresar nombre para B: ')
    b_list.append(b)

for i in range(num):
    print(f"A({i})={a_list[i]} B({i})={b_list[i]}", end=" ")
