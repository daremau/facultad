nombre_ven = input('Nombre del vendedor: ')
codigo_pago = input('Codigo de pago 1-contado, 2-cheque 3-tarjeta 4-crédito: ')
import_venta = int(input('Importe de venta: '))

if codigo_pago == 1:
    comision = import_venta * 0.1

elif codigo_pago == 2 or 3:
    comision = import_venta * 0.075

elif codigo_pago == 4:
    comision = import_venta * 0.05

print(f'El nombre del vendedor es:{nombre_ven} \n'
      f'Importe de venta: {import_venta} \n'
      f'Comision: {comision}')
