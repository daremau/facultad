import numpy as np


A = np.matrix([[65], [110], [10]])
B = np.matrix([[50], [90], [8]])
C = np.matrix([[75], [130], [12]])
D = np.matrix([[90], [170], [15]])

def resolver_sistema(matrizB):
    matrizA = np.matrix([[1, 1, 1], [1, 2, 4], [1 / 9, 1 / 6, 1 / 3]])
    
    inversa = np.linalg.inv(matrizA)

    x = inversa * matrizB

    return x

print('Residencia 1')
print(resolver_sistema(A))

print('Residencia 2')
print(resolver_sistema(B))

print('Residencia 3')
print(resolver_sistema(C))

print('Residencia 4')
print(resolver_sistema(D))