num_x = int(input('Valor de numero X: '))

if num_x > 100:
    num_r = (2 * (num_x ** 4)) - (7 * num_x) + 43

elif num_x < 100:
    num_r = abs(4 * (num_x**4) - (31 * num_x) + 9)

else:
    num_r = 2 * (num_x + 8)

print(num_r)