"""
u' = -a*u, u(t) is the fraction of particle that remains
u(0) = 1
"""

import ODEsolver as ODE, numpy as np, matplotlib.pyplot as plt
from math import*
#a)
class Decay:
    def __init__(self, a):
        self.a = a

    def __call__(self, u):
        self.u = u
        return -self.a*self.u

#b)
y = 500
u = []
for i in range(1,y):
    q = 1./i
    u.append(u)
    
u = np.array(u) 
a = np.linspace(log(2)/5600.0*u, y, 50)

#c)
f = Decay(a)

rk4 = ODE.RungeKutta4(Decay)
rk4.set_initial_condition(y)
rk41,rk42 = rk4.solve(a)

plt.plot(rk41,rk42)
plt.show()

