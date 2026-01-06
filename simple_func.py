import numpy as np

def myfunc(x):
    return 2*x

n = 100
xmin = 0.0
xmax = 10.

x = np.linspace(xmin, xmax, n+1)
y = np.sin(x)

z = myfunc(x) + y

print(z.sum())
