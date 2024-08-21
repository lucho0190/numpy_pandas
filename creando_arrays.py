import numpy as np

#lista = list (range(0,10)) #start 0, 10stop no se incluye
lista = np.arange(0,10)
lista = np.arange(0,20)
lista = np.arange(0,20,2) #paso de 2 en 2
lista = np.zeros(3) #array de 3 ceros
lista = np.zeros((10,10)) #crea un array de 10x10 ceros
lista = np.ones((10,5)) #crea un array de 10x5 unos
lista =np.linspace(0,10,10) #valor que inicia, valor que termina, cuantos elementos quiero generar
lista =np.linspace(0,10,100) #genera 100 valores entre 0 y 10
lista =np.eye(4) #matriz identidad 4x4
lista =np.random.rand() #genera un numero aleatorio entre 0 y 1
lista =np.random.rand(4) #genera 4 numeros aleatorios entre 0 y 1
lista =np.random.rand(4,5) #genera 4x5 numeros aleatorios entre 0 y 1
lista = np.random.randint(1,15) #genera un numero aleatorio entre 1 y 15
lista =np.random.randint(1,100,(10,10)) #genera 10x10 numeros aleatorios entre 1 y 100
print(lista)