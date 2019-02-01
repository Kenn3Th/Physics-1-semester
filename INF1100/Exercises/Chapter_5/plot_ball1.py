from numpy import *
from matplotlib.pyplot import *

v0 = 10
g = 9.81

t = linspace(0, 2*v0/g, 100)

y = v0*t - 0.5*g*t**2

plot(t,y)
xlabel('time (s)')
ylabel('heigth (m)')

show()
