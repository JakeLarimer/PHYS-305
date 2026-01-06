import numpy as np
import matplotlib.pyplot as plt

n = 1000
xmin = 0.0
xmax = 10.

x = np.linspace(xmin, xmax, n+1)
y = np.sin(x)

z = 2*x + y

print(z.sum())

plt.figure()
plt.plot(x, z)
plt.show()
