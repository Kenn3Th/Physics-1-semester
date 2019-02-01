import numpy as np, matplotlib.pyplot as plt
from numpy import arcsinh,cos,sin

rho = 0.5
x = np.linspace(-2,2,100)
S = lambda x: x**2
X = lambda x: x - 2*x*rho/np.sqrt(4*x**2+1)
Y = lambda x: x**2 + rho/np.sqrt(4*x**2+1)
P = np.array([X(x),Y(x)])
th = lambda x: 1.0/4*(2*x*np.sqrt(1+4*x**2) + arcsinh(2*x))/rho
bet = lambda x: 1.0/np.sqrt(1+4*x**2)
r = np.array([(rho*(cos(th(x))*2*x*bet(x) - sin(th(x))*bet(x)) + X(x)),\
               (rho*(-2*x*sin(th(x))*bet(x) - cos(th(x))*bet(x)) + Y(x))])
plt.plot(x,S(x))
plt.plot(P[0,:],P[1,:])
plt.plot(r[0,:],r[1,:])
plt.legend(['s(x)','(X(x),Y(x))','r(x)'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()


