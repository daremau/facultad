from random import randrange


import random

def tirar_moneda():
    rand_i = random.randrange(0, 1)
    moneda = ['Cara', 'Cruz']
    return moneda

N = int(input('Ingresar numero de lanzamientos: '))

i = 0
cara = 0
cruz = 0
while i < N:
    lanzamiento = tirar_moneda()
    
    if lanzamiento == 'Cara':
        cara += 1
    elif lanzamiento == 'Cruz':
        cruz += 1
    
    i += 1

prob_cruz = cruz / N
prob_cara = cara / N
