import numpy as np, matplotlib.pyplot as plt
from numpy import cos, sin, exp, pi

t = np.linspace(0,4*pi,100)
def r(t):
    return exp(-t)*np.array([cos(t),sin(t)])

x,y = r(t)

plt.plot(x,y)
plt.axis('equal')
plt.show()
