lad1 = int(input('Valor del 1er lado: '))
lad2 = int(input('Valor del 2do lado: '))
lad3 = int(input('Valor del 3er lado: '))

semi_p= (lad1 + lad2 + lad3)/2

area = (semi_p * (semi_p - lad1)*(semi_p - lad2) * (semi_p - lad3))**0.5

print(f'Los valores de los lados son: {lad1}, {lad2}, {lad3} \n'
      f'EL perimetro es {semi_p} y el area es {area}')

