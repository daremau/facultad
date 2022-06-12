nombre = input('Ingrese su nombre: ')
operacion = input('1-Consultar saldo, 2-Depositar saldo, 3-Retirar saldo: ')

saldo = 1000
if operacion == '1':
    print(f'El balance de su cuenta es{saldo}')

elif operacion == '2':
    monto = int(input('Monto a depositar: '))
    nuevo_saldo = saldo + monto
    print(f'Saldo anterior: {saldo}\n'
          f'Monto depositado: {monto}\n'
          f'Saldo actual: {nuevo_saldo}')

elif operacion == '3':
    mont_retirar = int(input('Monto a retirar: '))
    if mont_retirar > saldo:
        print('El monto a retirar es mayor que el saldo actual.')
    
    else:
        nuevo_saldo = saldo - mont_retirar
        print(f'Saldo anterior: {saldo}\n'
            f'Monto retirado: {mont_retirar}\n'
            f'Saldo actual: {nuevo_saldo}')

else:
    print('Elija una de las tres opciones disponibles')