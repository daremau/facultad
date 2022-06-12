n = int(input('dimension: '))

vector_a, vector_b, vector_c = [], [], []

for i in range(n):
    num_a = int(input('numero a: ')) 
    num_b = int(input('numero b: '))
   
    vector_a.append(num_a)
    vector_b.append(num_b)

a, b = 0, 0
for i in range(n * 2):
    if i % 2 == 0:
        vector_c.append(vector_a[a])
        a += 1
    else:
        vector_c.append(vector_b[b])
        b += 1
    