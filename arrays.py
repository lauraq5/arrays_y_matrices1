import random
x = [None]*10
# processing
for i in range(10):
    x[i]= random.random()
print(x[i]) 
# output

suma = 0
vector = [None]*5
# processing
for i in range(5):
    a = int(input("Dame un elemento"))
vector[i] = a
suma += vector[i]
# output
print("La suma de los elementos del vector es:", suma)

salarios = [None]*5
empleados = [None]*5
ps = 0
resultado = 0
# processing
for i in range(5):
    empleados[i] = input("Nombre de empleado")
    salarios[i] = int(input("Salario de empleado: "))
    ps += salarios[i]
ps = ps / 5
for i in range(5):
    if salarios[i] > ps:
        resultado += 1
# output
print("Número de empleados que ganan más del ps:", resultado)

mayor = -(100**10)
menor = 100**10
# input
n = int(input("Número de elementos: "))
# processing
vector = [None]*n
for i in range(n):
    print("posicion", i)
vector[i] = int(input("Valor: "))
if vector[i] > mayor:
    mayor = vector[i]
    pos_mayor =i
if vector[i] < menor:
    menor = vector[i]
    pos_menor = i
# output
print("Valor del mayor:", mayor)
print("Posición del mayor:", pos_mayor)
print("Valor del menor:", menor)
print("Posición del menor:", pos_menor)


norma = 0
# input
n = int(input("Número de elementos del vector: "))
# processing
vector = [None] * n
for i in range(n):
    print("posicion", i)
    vector[i] = int(input("valor"))
for i in range(n):
    norma = norma + vector[i]**2
    norma = norma**0.5
# output
print("Vector generado:", vector)
print("La magnitud del vector es:", norma)


resultado = 0
# input
n = int(input("Número de elementos de los vectores: "))

# processing
vector1 = [None] * n
print("Elementos del segundo vector:")
for i in range(n):
    print("posicion:", i)
    vector1[i] = int(input("Valor: "))
    vector2 = [None] * n
print("Elementos del segundo vector:")
for i in range(n):
    print("posicion:", i)
    vector2[i] = int(input("Valor: "))
producto=0
for i in range(n):
    producto += vector2[i]*vector1[i]
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("El producto punto entre los dos vectores es:", resultado)

M = [[1,2,3], [4,5,6], [7,8,9]]
# processing
for i in range(3):
    for j in range(3):
        print((M)[i][j], end=" ")
        print(M[i][j], end=" ")
print() # output


import random
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
for j in range(n):
    M[i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ") # output
print()


import random
suma = 0
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
for j in range(n):
    M[i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
print()
for i in range(m):
    for j in range(n):
        suma = suma + M[i][j]
# output
print("Suma de los elementos de la matriz:", suma)


import random
suma = 0
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
for j in range(n):
    [i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
print()

if m == n:
    for i in range(m):
        for j in range(n):
            if i == j:
                suma = suma + M[i][j]
                print("Resultado de la traza:", suma)
else:
    print("No existe una diagonal principal") # output


import random

128

suma = 0
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
for j in range(n):
    M[i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
print()
if m == n:
    for i in range(m):
        for j in range(n):
            if i + j == m-1:suma = suma + M[i][j]
            print("Suma de los elementos de la diagonal secundaria: ", suma) # output
else:
    print("No existe una diagonal secundaria") # output


import random
suma = 0

129

M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
for j in range(n):
    M[i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
print()
if m == n:
    for i in range(m):
        for j in range(n):
            if i > j:
                suma = suma + M[i][j]
                print("Suma de los elementos de la triangular inferior: ", suma) # output
else:
    print("No existe triangular inferior") # output

import random
suma = 0
M = []

130

# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
for j in range(n):
    M[i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
print()
if m == n:
    for i in range(m):
        for j in range(n):
            if i < j:
                suma = suma + M[i][j]
                print("Suma de los elementos de la triangular inferior: ", suma) # output
else:
    print("No existe triangular inferior") # output   


b = []
c = []
M = []
# input
m = int(input("Filas de la matriz: "))

131
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
for j in range(n):
    M[i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
print()
for i in range(m):
    for j in range(n):
        if M[i][j] % 2 == 0:
            b.append(M[i][j])
else:
    c.append(M[i][j])

# output
print("Elementos pares de la matriz:", b)
print("Elementos impares de la matriz:", c)

import random
suma = 0
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):

132

M.append([])
for j in range(n):
    M[i].append(random.randint(1,9))
for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
print()
for i in range(1, m-1):
    suma += M[i][0] + M[i][n-1]
for j in range(n):
    suma += M[0][j] + M[m-1][j]
print("Suma de los elementos periféricos de la matriz:", suma) # output


