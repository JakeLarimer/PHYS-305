import numpy as np

# Integrate the function f(x) (1-x^2)^(-0.5) from -1 to 1 in n steps.

def gauss_cheb(func, n):
    x = np.zeros(n)
    w = np.zeros(n)
    for i in range(n):
        x[i] = np.cos((2*i+1)*np.pi/(2.*n))
        w[i] = np.pi/n 

    sum = 0
    for i in range(n):
        sum += w[i]*func(x[i])
    return sum

def func(x):
    return 1.0

n = 10
integral = gauss_cheb(func, n)
print('integral =', integral, ' error =', integral-np.pi)
