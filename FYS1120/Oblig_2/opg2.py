import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from seaborn import*

e = -1.6*10**(-19)     #elektronladning
me = 9.11*10**(-31)    #elektronmasse

T = 30*10**(-12)         #fra t0 til T
dt = 10**(-15)           #tidssteg
N = int(T/float(dt))     #antall tidssteg
r = np.zeros((3,N))      #posisjonsvektor
v = np.zeros_like(r)     #hastighetsvektor
t = np.linspace(0,T-dt,N)#array med likt fordelt tid dt
#initialverdier
v[:,0] = (10*10**3,0,0)

B = np.array((0,0,2))  #Magnetfelt 

#Euler-Cromer
for i in xrange(N-1):
    Fb = e*(np.cross(v[:,i],B))
    a = Fb/me
    v[:,i+1] = v[:,i] + a*dt
    r[:,i+1] = r[:,i] + v[:,i+1]*dt
#plott
plt.subplot(2,1,1)
plt.plot(t,r[0,:],t,r[1,:],t,r[2,:])
plt.legend(['rx','ry','rz'])
plt.title('Posisjons graf')
plt.ylabel('Posisjon [m]')
plt.subplot(2,1,2)
plt.plot(t,v[0,:],t,v[1,:],t,v[2,:])
plt.legend(['vx','vy','vz'])
plt.title('Hastighets graf')
plt.ylabel('Hastighet [m/s]')
plt.xlabel('tid [s]')
plt.savefig('opg2.png')

#3d-plott
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[0,:], r[1,:], r[2,:],'-', label='Elektron akselerasjon')
ax.set_xlabel('x-posisjon [m]')
ax.set_ylabel('y-posisjon [m]')
ax.set_zlabel('z-posisjon [m]')
plt.savefig('3dopg2.png')
plt.show()

