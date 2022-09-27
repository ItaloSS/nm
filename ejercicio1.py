import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3,3,100000)
y = [i*i for i in x]
fig, ax = plt.subplots()
ax.set_title(r"Energia Potencial")
ax.set_xlabel("$x$")
ax.set_ylabel(" U(x)")
plt.xlim([-3, 3])
plt.ylim([0, 10])
plt.plot(x,y,label = r'$ U= \frac{1}{2}kx^2 $ ')
plt.show()