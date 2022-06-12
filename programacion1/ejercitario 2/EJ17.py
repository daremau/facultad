mayor = None
nom_mayor, dir_mayor = '', ''
while True:
    nombre = input('Ingresar nombre: ')
    direc = input('Ingresar direccion: ')
    sueldo = int(input('Ingresar sueldo: '))

    if sueldo <= 0:
        break

    if mayor is None:
        mayor = sueldo
        nom_mayor = nombre
        dir_mayor = direc
    elif sueldo > mayor:
        mayor = sueldo
        nom_mayor = nombre
        dir_mayor = direc

print(f"El empleado con mayor sueldo es: {nom_mayor}\n"
      f"DIRECCION: {dir_mayor}")

