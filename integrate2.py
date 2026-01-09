import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

def fi(x):
    return np.sin(x)

def trapezoid(x, dx):
    sum = dx*f(x[0])/2.0 + dx*f(x[-1])/2.0
    sum += dx*f(x[1:-1]).sum()
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
    num_int = trapezoid(x, dx)
    true_int = fi(xmax)-fi(xmin)
    dxplot.append(dx)
    errplot.append(abs(num_int - true_int))
    n *= 2

plt.figure()
plt.plot(dxplot, errplot)
plt.loglog()
plt.xlabel('$\Delta$x')
plt.ylabel('error')
plt.show()
