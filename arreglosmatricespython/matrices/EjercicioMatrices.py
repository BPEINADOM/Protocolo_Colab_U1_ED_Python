# Creamos una matriz de 3 filas y 3 columnas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostramos la matriz
print("Matriz de 3x3:")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()

# Recorrido por filas
print("\nRecorrido por filas:")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()


# Recorrido por columnas
print("\nRecorrido por columnas:")

for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(matriz[i][j], end=" ")
    print()

# Sumamos todos los elementos de la matriz
suma = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        suma = suma + matriz[i][j]

print("\nSuma de todos los elementos:", suma)


# Intercambiamos la primera fila con la última fila
auxiliar = matriz[0]
matriz[0] = matriz[-1]
matriz[-1] = auxiliar


# Mostramos la matriz después del intercambio
print("\nMatriz después de intercambiar la primera y la última fila:")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()