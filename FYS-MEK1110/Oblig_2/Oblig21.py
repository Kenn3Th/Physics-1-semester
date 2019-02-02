import numpy as np, matplotlib.pyplot as plt
from seaborn import*
#opgitte verdier
m = 0.1       #kg
g = 9.81      #N, jordas gravitasjons akselerasjon
L0 = 1.0      #m
k = 20.0     #N/m
theta = np.radians(0)  #grader omgjort til radianer
dt = 0.0001    #tidssteg
time = 10.0   #tid
#Vektor verdiene som blir regnet ut i for loopen
n = int(round(time/dt))
t = np.zeros((n,1),float)
r = np.zeros((n,2),float)
v = np.zeros((n,2),float)
a = np.zeros((n,2),float)
#initial verdier
v[0] = np.array([3.0,0]) 
r[0] = np.array([L0*np.sin(theta),-L0*np.cos(theta)])

def K(q):
    if (q-L0) > 0:
        return k
    else:
        return 0
   
for i in range(n-1):
    lr = np.sqrt(r[i,0]**2 + r[i,1]**2)
    #lr = np.linalg.norm(r[i])
    a[i,:] = np.array([(-K(lr)*(1-L0/lr)*r[i,0])/m,-g-(K(lr)*(1-L0/lr)*r[i,1])/m])
    v[i+1,:] = v[i,:] + a[i,:]*dt
    r[i+1,:] = r[i,:] + v[i+1,:]*dt
    t[i+1] = t[i] + dt
       
#plot av grafene til pendelen
plt.plot(r[:,0],r[:,1])
plt.title('Pendulum')
plt.axis('equal')
plt.show()
"""
plt.subplot(3,1,1)
plt.plot(t,r[:])
plt.axis([0,5,-1.5,1.5])
plt.ylabel('posisjon')
plt.legend(['x-retning','y-retning'])
plt.title('Pendulum')
plt.subplot(3,1,2)
plt.plot(t,v[:])
plt.ylabel('Hastighet')
plt.legend(['x-retning','y-retning'])
plt.subplot(3,1,3)
plt.plot(t,a[:])
plt.ylabel('Akselerasjon')
plt.legend(['x-retning','y-retning'])
plt.axis([0,5,-10,20])
plt.xlabel('Tid [t]')
plt.show()
"""
