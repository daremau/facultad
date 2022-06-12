cat1 = int(input('Valor del 1er cateto: '))
cat2 = int(input('Valor del 2do cateto: '))

hip = (cat1**2 + cat2**2)**0.5

print(f'Los catetos son {cat1} y {cat2} y la hipotenusa es {hip:.2f}')
