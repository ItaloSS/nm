import matplotlib.pyplot as plt
import numpy as np

# fig0 = plt.figure()  # an empty figure with no Axes
# fig1, ax = plt.subplots()  # a figure with a single Axes
# fig2, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

#hay diferencias entre Axes Axis
#Axes incluye Axis objects no son lo mismo
#cada axes  tiene un metodo set_title y set_xlabel(ylabel

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig3, ax1 = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax1.scatter('a', 'b', c='c', s='d', data=data)
ax1.set_xlabel('entry a')
ax1.set_ylabel('entry b')
plt.show()