num = int(input('Ingresar numero de vendedores: '))

comision = 0
sum_comision = 0
for i in range(num):
    nombre = input('Ingrese el nombre: ')
    impor_vent = int(input('Ingrese el importe de venta: '))
    num_libros = int(input('Ingrese la cantidad de libros: '))

    if num_libros <= 50:
        comision = impor_vent * 0.03

    elif num_libros < 80:
        comision = impor_vent * 0.05
    
    elif 80 <= impor_vent < 150:
        comision = impor_vent * 0.1
    
    else:
        comision = impor_vent * 0.15
    
    print(f'El vendedor {nombre} debe recibir una comision de: {comision}')
    
    sum_comision += comision

print(f'El total de comisiones a pagar es: {sum_comision}')