'''
ANALISIS DEL PROBLEMA:
    Hallar en cuantos meses el monto X con interes mensual T supere en mas del 30% al monto inicial.

BUSQUEDA DE RESULTADOS:
    -Utilizar la formula de interes compuesto S = P (1 + i) ^ n
        S = valor final
        P = capital
        i = interes
        n = periodo
    -Despejando n queda: n = Ln(S / P) / Ln(1 + i)
'''

# REDACCION DEL ALGORITMO:
import math

def tiempo_de_interes_compuesto(credito, interes):
    monto_final = credito * 1.3
    periodo = math.log(monto_final / credito) / math.log(1 + interes)

    return f"Deberan transcurrir {math.ceil(periodo)} meses."

print(tiempo_de_interes_compuesto(1000, 0.01))