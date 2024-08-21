import numpy as np
#Generamos números aleatorios entre 1 y 9 con una estructura de 3x2
arr = np.random.randint(1,10,(3,2))
#imprimir la forma original del arreglo
print("Forma original: ", arr.shape)
print(arr)
#cambiamos la forma del arreglo a una forma de (1,6)
arr_reshaped = arr.reshape(1,6)
#imprimimos el arreglo después del cambio de forma
print("Arreglo después de reshape:", arr_reshaped)  