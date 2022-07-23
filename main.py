import matplotlib.pyplot as plt
import numpy as np

y = lambda x: x
fig = plt.subplots()
x = np.linspace(0, 5, 100)
plt.plot(x, y(x))
ax = plt.gca()
ax.set_xlabel("Ось X", fontsize=15, color='red')
ax.set_ylabel("Ось Y", fontsize=15, color='green')
plt.show()
