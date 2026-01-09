import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

def fi(x):
    return np.sin(x)

def basic(x, dx):
    sum = dx*f(x[:]).sum()
    return sum
             
xmin = 0.0
xmax = 10.0
n = 10
nmax = 10000
dxplot = []
errplot = []
while n < nmax:
    x = np.linspace(xmin, xmax, n+1)
    dx = (xmax-xmin)/n
    num_int = basic(x, dx)
    true_int = fi(xmax)-fi(xmin)
    errplot.append(abs(num_int - true_int))
    dxplot.append(dx)
    n *= 2

print(dxplot, errplot)
plt.figure()
plt.plot(dxplot, errplot)
plt.loglog()
plt.xlabel('$\Delta$x')
plt.ylabel('error')
plt.show()
