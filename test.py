from tokenize import Double
import numth as nm
from random import *
import numpy as np
import matplotlib.pyplot as plt
def oscilador_forzado(X,t):
    Y = X.copy()
    #en X[0] tenemos la posicion(inicial en un principio)
    #en X[1] tenemos la velocidad(inicial en un principio)
    #en Y[0] se guarda la posicion, como varia es en funcion de la velocidad
    #en Y[1] se guarda la velocidad, como varia es en funcion de la funcion aceleracion
    Y[0] = X[1]
    Y[1] = -(0.1/(9.8*9.8))*X[1]  -np.sin(X[0]) - np.sin(t)*np.cos(X[0])/9.8
    return Y
osf = nm.Num_meth(oscilador_forzado,0.05,0.0,60)
fig, ax = plt.subplots()
ax.set_title("s")
ax.set_ylabel(r"$\dot{\theta}$")
ax.set_xlabel(r'$\theta$')
for i in range(4):
    cond_iniciales = np.array([3*i,-random()])
    D = osf.RK4(cond_iniciales,False,"dat")
    ax.plot(D[1],D[2],'-',label="{}".format(i))
    ax.legend()
    
#plt.xlim([-5, 5])
#plt.ylim([-5, 5])
plt.show()
