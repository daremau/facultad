num_a = int(input('Valor del numero A: '))
num_b = int(input('Valor del numero B: '))
num_c = int(input('Valor del numero C: '))

num_h = None
if num_c >= 0:
    num_h = (num_a ** 2 + num_b ** 2)**0.5
elif num_a > num_b:
    num_h = abs((3 * num_a - 7 * num_b)/num_c)
else:
    print(f'Los valores de A, B y C son: ', num_a, num_b, num_c)

if num_h is not None:
    print(f'El valor de H es {num_h}')