import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from seaborn import*

q = 1.6*10**(-19)     #elektronladning
me = 9.11*10**(-31)    #elektronmasse
mp = 1.67*10**(-27)    #protonmasse

T = 300*10**(-9)          #fra t0 til T [s]
dt = 100*10**(-15)        #tidssteg 
N = int(T/float(dt))      #antall tidssteg  
r = np.zeros((3,N))       #posisjonsvektor  [m]
v = np.zeros_like(r)      #hastighetsvektor [m/s]
t = np.linspace(0,T-dt,N) #array med likt fordelt tid dt
d = 90*10**(-6)           #valley gap [m]
r_D = 1                   #radius [m]

#initialverdier
v[:,0] = (0,0,0)
E0 = (25*10**3)/float(d)

B = np.array((0,0,2))  #Magnetfelt

omega = (q*B[2])/mp
    
#Euler-Cromer
for i in xrange(N-1):
    Fb = q*(np.cross(v[:,i],B))  #Magnetisk kraft
    E = np.zeros(3)              #elektriskfelt
    if -0.5*d<r[0,i]<0.5*d:
        E[0] = E0*np.cos(omega*t[i])
    else:
        E = 0
                                
    if np.linalg.norm(r[:,i]) < r_D:
        a = (Fb+E*q)/mp
    else:
        a = 0
    v[:,i+1] = v[:,i] + a*dt
    r[:,i+1] = r[:,i] + v[:,i+1]*dt

v_u = np.linalg.norm(v[:,-1])    
print 'Unnslipps hastighet = %.2f' %v_u

       
#plott
plt.plot(t,r[0,:],t,r[1,:],t,r[2,:])
plt.legend(['x','y','z'])
plt.title('Posisjon')
plt.xlabel('Tid [s]')
plt.ylabel('Posisjon [m]')
plt.savefig('3d_pos.png')
plt.show()
plt.plot(t,v[0,:],t,v[1,:],t,v[2,:])
plt.title('Hastighet')
plt.legend(['vx','vy','vz'])
plt.xlabel('Tid [s]')
plt.ylabel('Hastighet [m/s]')
plt.savefig('3d_hast.png')
plt.show()

"""
#3d-plott
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[0,:], r[1,:], r[2,:],'-', label='Elektron akselerasjon')
ax.set_xlabel('x-posisjon [m]')
ax.set_ylabel('y-posisjon [m]')
ax.set_zlabel('z-posisjon [m]')
plt.savefig('3dopg3.png')
plt.show()
"""
