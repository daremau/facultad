mayor, menor_edad = None, None
ventas_m, ventas_h, m, h = 0, 0, 0, 0
while True:
    id = int(input('Ingresar cedula: '))
    if id == -111:
        break
    nombre = input('Ingresar nombre: ')
    catg = int(input('Ingresar la categoria(1-5): '))
    sexo = int(input('Ingresar sexo(1:masculino/2:femenino)): '))
    imprt_vent = int(input('Ingresar el importe de venta: '))
    edad = int(input('Ingresar edad: '))

    if sexo == 2:
        ventas_m += imprt_vent
        m += 1
        if catg == 2:
            if mayor == None:
                mayor = imprt_vent
            elif mayor < imprt_vent:
                mayor = imprt_vent
    elif sexo == 1:
        ventas_h += imprt_vent
        h += 1
    elif catg == 4:
        if menor_edad == None:
            menor_edad = edad
        elif menor_edad > edad:
            menor_edad = edad

print(f"El mayor de los importes de venta de las empleadas de la ferretería de la categoría 2: {mayor}\n"
f"El promedio de los importes de venta de las empleadas mujeres: {ventas_m/m}\n"
f"La cantidad de empleadas mujeres: {h}\n"
'\n'
f"La menor edad de los empleados de la categoría 4: {menor_edad}\n"
f"El promedio de venta de los varones: {ventas_h}\n"
f"La cantidad de empleados varones: {h}")