import random

# Creamos un arreglo de 10 posiciones
numeros = [0] * 10

# Generamos un valor aleatorio para cada posición
for i in range(len(numeros)):

    # Generamos un número aleatorio entre 1 y 50
    numeros[i] = random.randint(1, 50)

# Mostramos el arreglo generado
print("Arreglo generado:")

for i in range(len(numeros)):
    print(numeros[i], end=" ")

    

# Recorrido con for clásico
print("\nRecorrido con for clásico:")

for i in range(len(numeros)):
    print(numeros[i], end=" ")

# Recorrido con for-each
print("\nRecorrido con for-each:")

for numero in numeros:
    print(numero, end=" ")


# Cambiamos los valores impares por cero
for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        numeros[i] = 0

# Multiplicamos cada valor por su índice
for i in range(len(numeros)):
    numeros[i] = numeros[i] * i

# Mostramos el arreglo modificado
print("\nArreglo modificado:")

for i in range(len(numeros)):
    print(numeros[i], end=" ")