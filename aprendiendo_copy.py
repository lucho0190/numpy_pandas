import numpy as np
arr = np.arange(0,11)
print(arr)
trozo_de_array = arr[0:6]
print(trozo_de_array)
# A todos mi array quiero quitar los valores y dejarlos en cero
trozo_de_array[:] = 0
print(trozo_de_array)
# Si ahora imprimimos el array completo, todos los valores están en cero
print(arr)

# Para solucionar esto utilizamos copy
arr_copy = arr.copy()
arr_copy[:] = 0
print(arr_copy)
#No obstante el array original no se ha modificado
print(arr)