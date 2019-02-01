import numpy as np, matplotlib.pyplot as plt

def RK2(f, U0, T, n):
    t = np.zeros(n+1); u = np.zeros(n+1)
    t[0] = 0; u[0] = U0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt*f(u[k],t[k])
        K2 = dt*f(u[k]+0.5*K1,t[k]+0.5*dt)
        u[k+1] = u[k] + K2
    return u, t
    
f = lambda t,x: x**2
ex = lambda t,x:1/3.*x**3

t = np.linspace(0,5,20)
N = 3; N2 = 8; T1 = 4; u = 0
solve, solve1 = RK2(f, u, T1, N)
cl, cl1 = RK2(f, u, T1, N2)

plt.subplot(2,1,1)
plt.plot(t,ex(0,t),'black', linewidth = 2.5)
plt.plot(solve1, solve, 'ro-')
plt.axis([0,6.5,0,25])
plt.ylabel('f(x)')
plt.xlabel('X')
plt.legend(['Exact','RK2 stor dt'])
plt.title('Runge Kutta 2 vs Exact')
plt.subplot(2,1,2)
plt.plot(t,ex(0,t),'black', linewidth = 2.5)
plt.plot(cl1,cl ,'yo-')
plt.legend(['Exact','RK2 liten dt'])
plt.xlabel('X')
plt.ylabel('f(x)')
plt.axis([0,6.5,0,25])

plt.show()

"""
Terminal> python RungeKutta2_func.py
"""
