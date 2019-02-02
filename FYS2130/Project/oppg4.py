import numpy as np, matplotlib.pyplot as plt
from classRungeKutta4 import*

#konstanter
m = 0.5         #masse [kg]
k = 1           #fjaerkraft  [N/m]
T = 200.0       #tid [s]
dt = 1e-2       #tidssteg
N = int(T/dt)   #antall tidssteg
t = np.linspace(0,T,N)
F = 0.7         #paatrukket kraft [N]
b = 0           #motstand [kg/s]
omega = np.sqrt(k/m)
#omegaD = (13.0/8)*omega
omegaD = (2.0/(np.sqrt(5)-1))*omega
#array
x = np.zeros(N) #posisjon
v = np.zeros(N) #hastighet
#numerisk losning
#initialbetingelser
x[0] = 2.0        
v[0] = 0.0
pendulum = DrivenPendulum(F,omegaD,k,b,m)
solver = RungeKutta4(pendulum)
for i in xrange(N-1):
    x[i+1],v[i+1] = solver(x[i],v[i],t[i],dt)
    
#analytisk losning
xa = (2-(F/(k-m*omegaD**2)))*np.cos(omega*t) + \
  (F/(k-m*omegaD**2))*np.cos(omegaD*t)
va = -omega*(2-(F/(k-m*omegaD**2)))*np.sin(omega*t) - \
  (omegaD*F/(k-m*omegaD**2))*np.sin(omegaD*t)
       
plt.plot(t,x)
#plt.plot(t,xa)
#plt.legend(['Numerisk','Analytisk'])
plt.title('Posisjon mot hastighet')
plt.ylabel('Posisjon [m]')
plt.xlabel('Tid [s]')
plt.savefig('2numvsan.png')
plt.show()
