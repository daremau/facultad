num_a = int(input('Valor del numero A: '))
num_b = int(input('Valor del numero B: '))

producto = num_a * num_b

if producto < 50:
    num_r = abs(producto)
else:
    num_r = producto**0.5

print(f'EL valor de A es {num_a} y el de B es {num_b}\n'
      f'EL valor del numero R es {num_r}')


