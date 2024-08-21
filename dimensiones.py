import numpy as np

#Cero dimensiones
scalar = np.array(42)
print(scalar)
print(scalar.ndim)

#Una dimension
vector = np.array([1,2,3])
print(vector)
print(vector.ndim)

#Dos dimensiones
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.ndim)

#Mas de dos dimensiones - Tensor
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim)

#Agregar o eliminar dimensiones
vector = np.array([1,2,3],ndmin=10) #ndmin permite agregar dimensiones aunque este es unidimensional
print(vector)
print(vector.ndim)

#Expandir
expand = np.expand_dims(np.array([1,2,3]),axis=0) #axis en 0 permite expandir a nivel de filas y 1 a nivel de columnas
print(expand)
print(expand.ndim)

#Squeeze: se usa para exprimir o eliminar dimensiones innecesarias (eliminar dimensiones que no estás usando)
print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)