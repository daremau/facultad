descripcion = input('Descripcion del articulo: ')
precio_vie = int(input('Precio del artiulo: '))
proced = input('Procedencia: ')

if any(proced == i for i in ['4', '5', '6']):
    precio = precio_vie * 1.075

elif any(proced == i for i in ['2', '3']):
    precio = precio_vie * 0.95

elif proced == '7':
    precio = precio_vie * 1.1

elif proced == '1':
    precio = precio_vie * 0.9

print(f'DESCRIPCION: {descripcion}\n'
      f'PRECIO VIEJO: {precio_vie}\n'
      f'PRECIO NUEVO: {precio}')
