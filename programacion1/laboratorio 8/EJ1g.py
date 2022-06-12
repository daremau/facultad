num = int(input('Ingresar un numero: '))

a_list = []
b_list = []
for i in range(num):
    a = input('Ingresar nombre para A: ')
    a_list.append(a)
    b = input('Ingresar nombre para B: ')
    b_list.append(b)

print(a_list[2:6])
b_list.reverse()
print(b_list[2:6])