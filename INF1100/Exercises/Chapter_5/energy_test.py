from numpy import linspace
from matplotlib.pyplot import show, plot
import matplotlib.pyplot as plt
import sys

g = 9.81
v0 = float(sys.argv[1]) #fetching the first number
m = float(sys.argv[2])  #fetching the second number
t = linspace(0, 2*v0/g, 50)

y = v0*t - 0.5*g*t**2
Pe = m*g*y
v = v0 - g*t
ke = 0.5*m*v**2

plot(t, Pe)
plot(t, ke)
plot(t, Pe+ke)
plt.xlabel('energy')
plt.ylabel('time')
plt.legend(['Potensial energy', 'Kinetic energy', 'Total of energy'])
show()
    
