import numpy as np, matplotlib.pyplot as plt
from classRungeKutta4 import*

#konstaner
m = 1.0
k1, k2, k3 = 10.0, 3.0, 5.0
b1,b2 = 1.5, 10.0
b3 = np.sqrt(k3*m)*2
N = 10**3

#arrays
zo = np.zeros(N)          #posisjon
vo = np.zeros(N)          #hastighet
zk = np.zeros(N)          #posisjon
vk = np.zeros(N)          #hastighet
zu = np.zeros(N)          #posisjon
vu = np.zeros(N)          #hastighet
t = np.linspace(0,10,N)  #Periode
dt = t[1]- t[0]          #Tidssteg

#initialverdier
zo[0] = zk[0] = zu[0] = 0.1


#dempninger ...-kritisk
under = RungeKutta4(b1,k1,m)
over = RungeKutta4(b2,k2,m)
kritisk = RungeKutta4(b3,k3,m)
for i in range (N-1):
    zo[i+1],vo[i+1] = over.rk4(zo[i],vo[i],t[i],dt)
    zk[i+1],vk[i+1] = kritisk.rk4(zk[i],vk[i],t[i],dt)
    zu[i+1],vu[i+1] = under.rk4(zu[i],vu[i],t[i],dt)

plt.plot(t,zu,'--',t,zo,'--',t,zk)
plt.title('Demping')
plt.legend(['Underkritisk','Overkritisk','Kritisk'])
plt.xlabel('Tid[s]')
plt.ylabel('Utsvingning[m]')
#plt.savefig('kritiskesvingninger.png')
plt.show()
