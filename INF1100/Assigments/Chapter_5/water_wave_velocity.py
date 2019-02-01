import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, tanh

def c(b):
    g = 9.81
    s = 7.9*10**(-2)
    rho  = 1000
    h = 50
    return sqrt((g*b)/(2*pi)*(1 + s*(4*pi**2)/(rho*g*b**2))*tanh((2*pi*h)/b))

lmdA = np.linspace(0.001, 0.1, 100)
Lmda = np.linspace(1, 2000, 100)

q = np.zeros(len(lmdA)) #liten verdi av lambda
z = np.zeros(len(Lmda)) #stor verdi av lambda

for i in xrange(len(lmdA)):
    q[i] = c(lmdA[i])

for j in xrange(len(Lmda)):
    z[j] = c(Lmda[j])

plt.plot(q,"r")
plt.legend(['Liten Lambda'])
plt.title('Water wave velocity')
plt.ylabel('m/s')
plt.xlabel('m')
plt.show()

plt.plot(z)
plt.legend(['Stor Lambda'])
plt.title('Water wave velocity')
plt.ylabel('m/s')
plt.xlabel('m')
plt.show()
"""
Terminal> python water_wave_velocity.py
"""
