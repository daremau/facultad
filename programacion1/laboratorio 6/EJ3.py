mayor = None
nom_mayor = ''
menor = None
nom_menor = ''

suma_sueldo, suma_sueldo_h, suma_sueldo_m = 0, 0, 0
t, h, m = 0, 0, 0
while True:
    ci = int(input('Ingresar CI: '))
    if ci <= 0:
        break
    nombre = input('Ingresar nombe y apellido: ')
    sexo = int(input('Ingresar sexo(0:masculino, 1:femenino): '))
    sueldo = int(input('Ingresar sueldo: '))
    suma_sueldo += sueldo
    t += 1
    if sexo == 0:
        suma_sueldo_h += sueldo
        h += 1
        if mayor is None:
            mayor = sueldo
            nom_mayor = nombre
        elif sueldo > mayor:
            mayor = sueldo
            nom_mayor = nombre
    else:
        suma_sueldo_m += sueldo
        m += 1
        if menor is None:
            menor = sueldo
            nom_menor = nombre
        elif sueldo < menor:
            menor = sueldo
            nom_menor = nombre

print(f"El empleado varon que mas gana: {nom_mayor}, sueldo: {mayor}\n"
    f"La empleada que menos gana: {nom_mayor}, sueldo: {menor}\n"
    f"Sueldo promedio de los hombre: {suma_sueldo_h/h}\n"
    f"Sueldo promedio de las mujeres: {suma_sueldo_m/m}\n"
    f"Sueldo promedio total: {suma_sueldo/t}")