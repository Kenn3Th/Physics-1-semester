import numpy as np, matplotlib.pyplot as plt
from math import *

F = 400     # kraft Newton[N]
m = 80.0    # masse [kg]
p = 1.293   # [kg/m^3]
A = 0.45    # [m^2]
Cd = 1.2    # Drag koeffisienten
w = 0       # Luft hastighet
time = 8    # Tid sekunder[s] 
dt = 1./100 #dette er hva jeg har valgt som delta t
n = int(time/dt) 
a = np.zeros(n); t = np.zeros(n)
x = np.zeros(n); v = np.zeros(n)
x[0] = 0; v[0] = 0 #initial verdien til posisjon og hastighet
q = 0

for i in range(int(n-1)):
    a[i] = (400 - 0.5*p*Cd*A*(v[i]-w)**2)/m
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt
    t[i+1] = t[i] + dt
    if x[i+1] > 100:
        q = i + 1
        break

plt.subplot(3,1,1)      #lager tre separate grafer i samme plott
plt.title('Bevegelses diagram')
plt.plot(t[0:q],x[0:q]) #[0:q]=henter tall verdiene fra 0 til q
plt.ylabel('x [m]')
plt.subplot(3,1,2)
plt.plot(t[0:q],v[0:q])
plt.ylabel('v [m/s]')
plt.subplot(3,1,3)
plt.plot(t[0:q],a[0:q])
plt.ylabel('a [m/s^2]')
plt.xlabel('t [sekund]')
plt.show()

