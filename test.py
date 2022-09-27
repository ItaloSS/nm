from tokenize import Double
import numth as nm
import numpy as np

def oscilador_forzado(X,t):
    alpha = 1.0
    gamma = 1.0
    omega = 1.0
    Y = X.copy()
    #en X[0] tenemos la posicion(inicial en un principio)
    #en X[1] tenemos la velocidad(inicial en un principio)
    #en Y[0] se guarda la posicion, como varia es en funcion de la velocidad
    #en Y[1] se guarda la velocidad, como varia es en funcion de la funcion aceleracion
    Y[0] = X[1]
    Y[1] = gamma*np.cos(omega*t) -alpha*X[0]
    return Y
def pol(Y,t):
    # dx/dt = 5t
    Y_i = Y.copy()
    Y_i[0] = 5*t
    return Y_i




osf = nm.Num_meth(oscilador_forzado,0.005,0.0,30)
cond_iniciales = np.array([0,1])
osf.RK4(cond_iniciales)

