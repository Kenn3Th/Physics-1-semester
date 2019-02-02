import numpy as np, matplotlib.pyplot as plt
from RungeKutta4 import*

#konstanter
m = 1
N = 10**3

#arrays
t = np.linspace(0,10,N)
#underkritisk
zu = np.zeros(N)
vu = np.zeros(N)
bu = 1.5
ku = 10.0
#kritisk
zk = np.zeros(N)
vk = np.zeros(N)
kk=5.0
bk=np.sqrt(kk*m)*2
#overkritisk
zo = np.zeros(N)
vo = np.zeros(N)
ko = 3.0
bo = 10.0

#initialverdier
zu[0] = 1
vu[0] = 0
zk[0] = 1
vk[0] = 0
zo[0] = 1
vo[0] = 0
dt = t[1]-t[0]

#akselerasjon
def diffEq(x,v,t,b,k):
    a = -float(b)/m*v - float(k)/m*x
    return a
#Runge-Kutta
def rk4(x0,v0,t0,b,k):
    a1 = diffEq(x0,v0,t0,b,k)
    v1 = v0
    xHalv1 = x0 + v1 * dt/2.0
    vHalv1 = v0 + a1 * dt/2.0
    a2 = diffEq(xHalv1,vHalv1,t0+dt/2.0,b,k)
    v2 = vHalv1
    xHalv2 = x0 + v2 * dt/2.0
    vHalv2 = v0 + a2 * dt/2.0
    a3 = diffEq(xHalv2,vHalv2,t0+dt/2.0,b,k)
    v3 = vHalv2
    xEnd = x0 + v3 * dt
    vEnd = v0 + a3 * dt
    a4 = diffEq(xEnd,vEnd,t0 + dt,b,k)
    v4 = vEnd
    aMid = 1.0/6.0 * (a1 + 2*a2 + 2*a3 + a4)
    vMid = 1.0/6.0 * (v1 + 2*v2 + 2*v3 + v4)
    xEnd = x0 + vMid * dt
    vEnd = v0 + aMid * dt
    return xEnd, vEnd


for i in range(N-1):
    zu[i+1],vu[i+1] = rk4(zu[i],vu[i],t[i],bu,ku)
    zo[i+1],vo[i+1] = rk4(zo[i],vo[i],t[i],bo,ko)
    zk[i+1],vk[i+1] = rk4(zk[i],vk[i],t[i],bk,kk)

plt.plot(t,zu,'--',t,zo,'--',t,zk,'r')
plt.legend(['Underkritisk','Overkritisk','Kritisk'])
plt.xlabel('Tid[s]')
plt.ylabel('Utsvingning[m]')
plt.savefig('kritiskesvingninger.png')
plt.show()
