num = int(input('Ingresar un numero: '))

a_list = []
b_list = []
for i in range(num):
    a = input('Ingresar nombre para A: ')
    a_list.append(int(a))
    b = input('Ingresar nombre para B: ')
    b_list.append(int(b))

print(sum(a_list/len(a_list)))
print(sum(b_list))