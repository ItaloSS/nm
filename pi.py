import random
from math import *
from matplotlib import markers
import matplotlib.pyplot as plt

lista_cuadrado = []
lista_listacirculo = []
lista_x_circulo =[]
lista_y_circulo = []
lista_x_cuadrado = []
lista_y_cuadrado = []
for i in range(10**7):
    vector = (random.uniform(-1,1),random.uniform(-1,1))
    if (sqrt(vector[0]**2 + vector[1]**2) <= 1):
        lista_listacirculo.append(vector)
        lista_x_circulo.append(vector[0])
        lista_y_circulo.append(vector[1])
    else:
        lista_x_cuadrado.append(vector[0])
        lista_y_cuadrado.append(vector[1])
    #calcular pi
    lista_cuadrado.append(vector)
pi = (4*len(lista_listacirculo))/len(lista_cuadrado)

plt.title(str(pi))
plt.scatter(lista_x_circulo, lista_y_circulo, label = "circulo", color = "red")
plt.scatter(lista_x_cuadrado, lista_y_cuadrado, label = "cuadrado", color = "green")  # Plot some data on the axes.
plt.show()
