import numpy as np
import matplotlib.pyplot as plt
from math import sin, exp, pi

def f(x, t):
    return exp(-(x - 3*t)**2)*sin(3*pi*(x - t))

x = np.linspace(-4, 4, 1001)
h = np.zeros(len(x))

for i in xrange(len(x)):
    h[i] = f(x[i], 0)

plt.plot(h)
plt.title('Wavwpacket')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(['f(x,t) = exp(-(x - 3*t)**2)*sin(3*pi*(x - t)'])
plt.axis([0, 1000,-1, 1.5])
plt.show()

"""
Terminal> python plot_wavepacket.py
"""
