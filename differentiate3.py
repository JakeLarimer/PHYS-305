import math
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x)

def fp(x):
    return -math.sin(x)

dxplot = []
dplot1 = []
dplot2 = []
errplot1 = []
errplot2 = []

x = 1.0
dx = 1.0
while dx > 1.e-15:
    deriv1 = (f(x+dx)-f(x))/dx
    deriv2 = (f(x+dx)-f(x-dx))/(2*dx)
    dxplot.append(dx)
    dplot1.append(deriv1)
    dplot2.append(deriv2)
    errplot1.append(abs(deriv1-fp(x)))
    errplot2.append(abs(deriv2-fp(x)))
    dx /= 2

fig, ax = plt.subplots(1, 2, figsize=(10,5))
plt.subplots_adjust(wspace=0.25)
fig.suptitle('Comparison of one-sided and centered derivative estimates', y=0.965)

ax[0].semilogx(dxplot, dplot1, label='1-sided')
ax[0].semilogx(dxplot, dplot2, label='centered')
ax[0].set(xlabel='$\Delta$x', ylabel='derivative')
ax[0].legend()

ax[1].loglog(dxplot, errplot1, label='1-sided')
ax[1].loglog(dxplot, errplot2, label='centered')
ax[1].set(xlabel='$\Delta$x', ylabel='|error|')
ax[1].legend()

plt.show()
