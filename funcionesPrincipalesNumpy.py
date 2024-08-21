import numpy as np

# definimos números aleatorios del 1 al 20  en un vector
arr = np.random.randint(1, 20, 10)

# imprimimos el vector
print(arr)

# ahora lo llevamos a una estructua matricial
matriz = arr.reshape(2,5)

print(matriz)

# con max voy a traer el número más grande la matriz
maximo = arr.max()

print(maximo)

maximo = matriz.max()

print(maximo)

# creamos un array de dos dimensiones

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# ¿Que pasa cuando queremos unir el array a con el array b?

c = np.concatenate((a, b), axis=0) # axis = 0  nos indica que los array se apilan por filas uno debajo del otro, con axis = 1 se apilan por columnas
print(c)

