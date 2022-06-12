num_a = int(input('Valor de a: '))
num_b = int(input('Valor de b: '))
num_c = int(input('Valor de c: '))
num_d = int(input('Valor de d: '))

num_r = (((num_a - num_b)**2)/num_c) - (((num_a - num_b)**2)/(num_c - num_a))

print(f'Para a={num_a} b={num_b} c={num_c} d={num_d} el numero R es: {num_r}')