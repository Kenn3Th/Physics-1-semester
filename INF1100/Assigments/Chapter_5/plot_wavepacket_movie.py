import glob, os
for plot_wavepacket_movie in glob.glob('tmp*.png'):
    os.remove(plot_wavepacket_movie)
    
import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return np.exp(-(x - 3*t)**2)*np.sin(3*np.pi*(x - t))

x = np.linspace(-6, 6, 1001)
t_values = np.linspace(-1, 1, 61)

plt.ion()
y = f(x, t_values[0])
lines = plt.plot(x, y)
plt.axis([x[0], x[-1], -1, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wavepacket')

counter = 0
for t in t_values:
    y = f(x, t)
    lines[0].set_ydata(y)
    plt.legend(['t = %4.2f' %t])
    plt.draw()
    plt.savefig('tmp_%04d.png' %counter)
    counter += 1
    plt.pause(0.01)
    
plt.show()

"""
Terminal>python plot_wavepacket_movie.py
"""
