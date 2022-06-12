num_a = int(input('Valor Numero A:'))
num_b = int(input('Valor numero B: '))
num_c = int(input('Valor numero C: '))

menor = min(num_a, num_b, num_c)
mayor = max(num_a, num_b, num_c)
medio = (num_a + num_b + num_c) - menor - mayor

print(f'Los numeros son {num_a}, {num_b}, {num_c} en orden creciente: {menor}, {medio}, {mayor}')