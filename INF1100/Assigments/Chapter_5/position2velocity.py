import numpy as np
import matplotlib.pyplot as plt

b = []
c = []

infile = open('pos.dat', 'r')
s = float(infile.readline())
for line in infile:
    dig = line.split()
    b.append(float(dig[0]))
    c.append(float(dig[1]))
infile.close()

x = np.array(b)
y = np.array(c)

plt.plot(x,y)
plt.title('2d plot of position')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

t = np.linspace(0, s, len(x))

vx = np.zeros(len(x))
for i in xrange(len(x)):
    vx[i] = (x[i] - x[i-1])/s

vy = np.zeros(len(y))
for i in xrange(len(y)):
    vy[i] = (y[i] - y[i-1])/s

plt.subplot(2,1,1)
plt.plot(t, vx)
plt.ylabel('v(x)')
plt.title('Velocity in x-direction')
plt.subplot(2,1,2)
plt.plot(t, vy, 'r')    
plt.xlabel('time')
plt.ylabel('v(y)')
plt.title('Velocity in y-direction')
plt.show()

"""
Terminal>
"""
