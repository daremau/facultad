nombre = input('Nombre del empleado: ')
horas = int(input('Horas trabajadas: '))
tarifa = int(input('Tarifa por hora: '))
impuesto = int(input('Tasa de impuesto: '))

if horas > 40:
    salario_bruto = horas * (tarifa * 1.5)
else:
    salario_bruto = horas * tarifa

descuento = salario_bruto * impuesto/100
ips = salario_bruto * 0.095

salario = salario_bruto - descuento - ips

print(f'NOMBRE DEL EMPLEADO: {nombre}\n'
      f'SALARIO BRUTO: {salario_bruto}\n'
      f'DESCUENTO POR LOS IMPUESTOS: {descuento}\n'
      f'DESCUENTO PARA I.P.S: {ips}\n'
      f'SALARIO A COBRAR {salario}')
