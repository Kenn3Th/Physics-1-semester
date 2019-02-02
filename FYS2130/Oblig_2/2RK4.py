import numpy as np, matplotlib.pyplot as plt

#akselerasjon
def diffEq(x,v,t):
    if t <30:
        a = (F/m)*np.cos(np.sqrt((k/m)*0.8-(b**2/(2*m**2)))*t)-b/m*v-k/m*x
    else:
        a = -float(b)/m*v - float(k)/m*x
    return a 

#Runge-Kutta
def rk4(x0,v0,t0):
    a1 = diffEq(x0,v0,t0)
    v1 = v0
    xHalv1 = x0 + v1 * dt/2.0
    vHalv1 = v0 + a1 * dt/2.0
    a2 = diffEq(xHalv1,vHalv1,t0+dt/2.0)
    v2 = vHalv1
    xHalv2 = x0 + v2 * dt/2.0
    vHalv2 = v0 + a2 * dt/2.0
    a3 = diffEq(xHalv2,vHalv2,t0+dt/2.0)
    v3 = vHalv2
    xEnd = x0 + v3 * dt
    vEnd = v0 + a3 * dt
    a4 = diffEq(xEnd,vEnd,t0 + dt)
    v4 = vEnd
    aMid = 1.0/6.0 * (a1 + 2*a2 + 2*a3 + a4)
    vMid = 1.0/6.0 * (v1 + 2*v2 + 2*v3 + v4)
    xEnd = x0 + vMid * dt
    vEnd = v0 + aMid * dt
    return xEnd, vEnd


#konstanter
m = 0.1
k = 10.0
b = 0.04
F = 0.1
N = 10**3
#arrays
z = np.zeros(N)
v = np.zeros(N)
t = np.linspace(0, 50, N)

#initial betingelser
z[0] = 0     #[m]
v[0] = 0       #[m/s]
dt = t[1]-t[0] #tidssteg

#iterasjoner i Runge-Kutta 4
for i in range(N-1):
    z[i+1], v[i+1] = rk4(z[i],v[i],t[i])

plt.plot(t,z)
plt.title('$\omega_f$ ulik $\omega_0$')
plt.xlabel('Tid[s]')
plt.ylabel('Utsvingning [m]')
plt.savefig('w0ulikwf.png')
plt.show()
