import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

def fi(x):
    return np.sin(x)

def simpson(x, dx):
    return dx*(f(x[0]) + 4*f(x[1:-1:2]).sum() + 2*f(x[2:-2:2]).sum() + f(x[-1]))/3
             
xmin = 0.0
xmax = 10.0
n = 10
nmax = 10000
dxplot = []
errplot = []
while n < nmax:
    x = np.linspace(xmin, xmax, n+1)
    dx = (xmax-xmin)/n
    dxplot.append(dx)
    num_int = simpson(x, dx)
    true_int = fi(xmax)-fi(xmin)
    errplot.append(abs(num_int - true_int))
    n *= 2

plt.figure()
plt.plot(dxplot, errplot)
plt.loglog()
plt.xlabel('$\Delta$x')
plt.ylabel('error')
plt.show()
