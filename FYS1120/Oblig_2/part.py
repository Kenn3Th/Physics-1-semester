import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

e = -1.6*10**(-19)
me = 9.11*10**(-31)
E = np.array((-1,-2,5))
F = E*e

T = 10**(-6)
dt = 10**(-9)
#dt2 = 10**(-7)
N = int(T/float(dt))
r = np.zeros((3,N))
v = np.zeros_like(r)
t = np.linspace(0,T-dt,N)

#Euler-Cromer
for i in xrange(N-1):
    a = F/me
    v[:,i+1] = v[:,i] + a*dt
    r[:,i+1] = r[:,i] + v[:,i+1]*dt

a = (-5*e)/me
rt = lambda t: 0.5*a*t**2

#plot(t,r[0,:],t,rt(t))
#legend(['Numerisk','Analytisk'])
plt.plot(t,r[0,:],t,r[1,:],t,r[2,:])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[0,:], r[1,:], r[2,:], label='Elektron akselerasjon')
plt.show()
