importe_total, comision_total = 0, 0
while True:
    ci = int(input('Ingresar CI: '))
    if ci == -111:
        break
    nombre = input('Ingresar nombre: ')
    impt_vent = int(input('Ingresar importe de venta: '))
    cantidad_lotes = int(input('Ingresar la cantidad de lotes vendidos:'))
    
    importe_total += impt_vent

    if cantidad_lotes <= 10:
        comision = 0.02
        comision_total = comision * impt_vent
    elif 10 < cantidad_lotes <= 20:
        comision = 0.035
        comision_total = comision * impt_vent
    elif cantidad_lotes > 20:
        comision = 0.05
        comision_total = comision * impt_vent

    print(f"Vendedor: {nombre}, CI: {ci}\n"
    f"Cantidad de lotes vendidos: {cantidad_lotes}\n"
    f"Importe de venta: {impt_vent}\n"
    f"Comision: {impt_vent * comision}\n")

print(f"Total general de importes vendidos: {importe_total}\n"
f"Total de comisiones: {comision_total}")
