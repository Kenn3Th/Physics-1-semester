from numpy import *
from matplotlib.pyplot import *
import sys

v0_list = sys.argv[1:]
g = 9.81

max_t = 0
max_y = 0

for v0 in v0_list:
    v0 = float(v0)
    t = linspace(0, 2*v0/g, 100)
    if max(t) > max_t:
        max_t = max(t)
    y = v0*t - 0.5*g*t**2
    if max(y) > max_y:
        max_y = max(y)
    plot(t,y,label='v0=%g' %v0)

xlabel('time (s)')
ylabel('heigth (m)')
legend()
axis([0, max_t, 0, 1.1*max_y])

show()
