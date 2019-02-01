import numpy as np, matplotlib.pyplot as plt
from numpy import arcsinh,cos,sin

"""
#plt.ion
for i in x:
    th = 1.0/4*(2*i*np.sqrt(1+4*i**2) + arcsinh(2*i))
    bet = 1.0/np.sqrt(1+4*i**2)
    r[i,:] = np.matrix([rho*(cos(th)*2*i*bet- sin(th)*bet + i - 2*i*rho*bet),\
                        rho*(-2*i*sin(th)*bet - cos(th)*bet + i**2 + rho*bet)])
    print r[i], i
    #plt.scatter(r[i,0],r[i,1])
    #plt.plot(x,S(x))
    #plt.axis([-1,1,-1,4])
    #plt.pause(0.0001)
    #plt.cla
"""

x = np.linspace(-2,2,100)
n = len(x)
#r = np.zeros((n,2))
th = lambda x: 1.0/4*(2*x*np.sqrt(1+4*x**2) + arcsinh(2*x))
bet = lambda x: 1.0/np.sqrt(1+4*x**2)
rho = 0.5
r = np.matrix([rho*(cos(th(x))*2*x*bet(x)- sin(th(x))*bet(x) + x - 2*x*rho*bet(x)), rho*(-2*x*sin(th(x))*bet(x) - cos(th(x))*bet(x) + x**2 + rho*bet(x))])
r = r.transpose()

"""
for i in range(1,n):
    h = abs(x[i]-x[i-1])
    r[i] = r[i-1] + h*(1-r[i-1]**2)
"""
plt.plot(r[:,0],r[:,1])
plt.show()
