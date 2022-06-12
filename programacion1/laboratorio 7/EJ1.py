h, m, t = 0, 0, 0
sueldo_h, sueldo_m, sueldo_total = 0, 0, 0
mayor = None
while True:
    id = int(input('Ingresar ID: '))
    if id <= 0:
        break
    nombre = input('Ingresar nombre: ')
    sexo = input('Ingresar sexo(M/F): ')
    sueldo = int(input('Ingresar sueldo: '))
    sueldo_total += sueldo
    t += 1

    if sexo.upper() == 'M':
        if mayor is None:
            mayor = sueldo
            nombre_mayor = nombre
        elif mayor < sueldo:
            mayor = sueldo
            nombre_mayor = nombre
        sueldo_h += sueldo
        h += 1

    elif sexo.upper() == 'F':
        sueldo_m += sueldo
        m += 1

print(f"EL EL EMPLEADO QUE MAS GANA ES: {nombre_mayor}, SUELDO: {mayor}\n"
    f"PROMEDIO SUELDO HOMBRES: {sueldo_h/h}\n"
    f"PROMEDIO SUELDO MUJERES: {sueldo_m/m}\n"
    f"PROMEDIO DE SUELDO TOTAL: {sueldo_total/t}")
