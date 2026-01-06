import math
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x)

def fp(x):
    return -math.sin(x)

x = 1.0
dx = 1e-3
deriv = (f(x+dx)-f(x-dx))/(2*dx)
print(x, deriv, fp(x), abs(deriv-fp(x)))
