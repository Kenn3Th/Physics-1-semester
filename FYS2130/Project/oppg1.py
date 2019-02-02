import numpy as np, matplotlib.pyplot as plt
from classRungeKutta4 import*

#konstanter
m = 0.5         #masse [kg]
k = 1           #fjaerkraft  [N/m]
T = 20.0        #tid [s]
dt = 1e-2       #tidssteg
N = int(T/dt)   #antall tidssteg
t = np.linspace(0,20,N)
F = 0           #paatrukket kraft [N]
b = 0           #motstand [kg/s]
omega = np.sqrt(k/m)
#array
x = np.zeros(N) #posisjon
v = np.zeros(N) #hastighet
#initialbetingelser
x[0] = 1        
v[0] = 0
pendulum = DrivenPendulum(F,omega,k,b,m)
solver = RungeKutta4(pendulum)
for i in xrange(N-1):
    x[i+1],v[i+1] = solver(x[i],v[i],t[i],dt)
   
plt.plot(x,v)
plt.title('Posisjon mot hastighet')
plt.xlabel('Posisjon [m]')
plt.ylabel('Hastighet [m/s]')
#plt.savefig('pvhb.png')
plt.show()

    

