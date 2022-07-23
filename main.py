import matplotlib.pyplot as plt
import numpy as np
y = lambda x: x**2
fig = plt.subplots()
x = [0, 2, 4, 6]
z = [1, 3, 5, 7]
print(x, z)
plt.plot(x, z, color='r', linestyle=':')
plt.plot(x, list(map(y, x)))
plt.title('График')
ax = plt.gca()
ax.set_xlabel("Ось X", fontsize=15, color='red')
ax.set_ylabel("Ось Y", fontsize=15, color='green')
plt.savefig('graph.png')
plt.show()
