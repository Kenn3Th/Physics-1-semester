#k)
import numpy as np, matplotlib.pyplot as plt

F = 400; fc = 488; fv = 25.8; m = 80.0; p = 1.293; A = 0.45; Cd = 1.2; w = 0
time = 9.3; dt = 1./1000; n = int(time/dt); tc = 0.67
a = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)
t = np.zeros(n)
v[0] = 0; x[0] = 0; t[0] = 0

D = lambda t,v: A*(1 - 0.25*np.exp(-(t/tc)**2))*0.5*p*Cd*(v-w)**2
Fv = lambda v: v*fv
Fc = lambda t: fc*np.exp(-(t/tc)**2)
                                    
for i in range(int(n-1)):
    a[i] = (F + Fc(t[i]) - Fv(v[i]) - D(t[i],v[i]))/m
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt
    t[i+1] = t[i] + dt
Fnet = F + Fc(t) - Fv(v) - D(t,v)                                                       
plt.plot(t,Fc(t),t,Fv(v),t,D(t,v),[0,9.3],[400,400])
plt.legend(['Initial Driving force', 'Physioligical limit','Air resistance','Driving Force'])
plt.axis([0,9.3,-10,600])
plt.show()


