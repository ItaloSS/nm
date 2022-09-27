import matplotlib.pyplot as plt
import numpy as np
#np.linespace retorna un intervalo 
#igualmente espaciado (inicio,final,puntos)
x = np.linspace(0,2*np.pi,200)

#sin(x) acepta np.array
y = np.sin(x)

#genera una figura por defecto
#(<Figure size 640x480 with 1 Axes>, <AxesSubplot:>)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()

