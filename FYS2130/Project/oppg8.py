import numpy as np
from classRungeKutta4 import*

#konstanter
k = 0.475       #fjaerkraft  [N/m]
g = -9.81       #m/s^2
T = 20.0         #tid [s]
dt = 1e-4       #tidssteg
N = int(T/dt)   #antall tidssteg
b = 1e-3        #motstand [kg/s]
xc = 2.5e-3
beta = 50       #s/m
rho = 1e3       #kg/m^3
#array
Psi = np.linspace(5.5e-5,7.5e-5,100)
t = np.linspace(0,T,N) #tid
x = np.zeros([100,N])  #posisjon
v = np.zeros([100,N])  #hastighet
m = np.zeros([100,N])  #masse
D = np.zeros([100,N])#tiden da draapen faller
for j,psi in enumerate(Psi):
    #initialbetingelser
    x[j][0] = 1e-3       
    v[j][0] = 1e-3
    m[j][0] = 1e-5
    for i in xrange(N-1):
        m[j][i+1] = m[j][i] + psi*dt
        dripp = Dripp(g,psi,b,k,m[j][i])
        solver = RungeKutta4(dripp)
        x[j][i+1],v[j][i+1] = solver(x[j][i],v[j][i],t[i],dt)
        if np.abs(x[j][i+1]) > xc:
            D[j][i] = t[i]
            dm = np.abs(beta*m[j][i+1]*v[j][i+1])
            if dm > m[j][i+1]:
                m[j][i+1] = 1e-5
            else:
                m[j][i+1] = m[j][i+1] + psi*dt - dm
            dx = ((3*dm**4)/(4*np.pi*rho*(m[j][i]**3)))**(1./3)
            if dx > np.abs(x[j][i+1]):
                dx = x[j][i+1]+1e-7
            x[j][i+1] = x[j][i+1] + dx
            
np.save('opg8',np.asarray([x,v,m,D]))
np.save('opg8t',np.asarray([t,Psi]))

