#Comparing Runge-Kutta4 to Euler's method
"""
dy/dx=1/(2*(y-1)) the same as y' = 1/(2*(y-1)), y(0) = 1 + sqrt(eps) ,
x element [0,4], eps = 1E-3 n = 4
exact = y(x) = 1 + sqrt(x + eps)
"""
import numpy as np, matplotlib.pyplot as plt, ODEsolver as ODE

epsi = 1E-3; y0 = 1 + np.sqrt(epsi)
n = np.linspace(0,4,100); q = np.linspace(0,4,260)
exact = lambda x: 1 + np.sqrt(x + epsi)
def f(y,x):
    return 1/(2*(y-1))

rk4 = ODE.RungeKutta4(f)
rk4.set_initial_condition(y0)
u,t = rk4.solve(n)

forEuler = ODE.ForwardEuler(f)
forEuler.set_initial_condition(y0)
u1,t1 = forEuler.solve(n)

plt.subplot(2,1,1)
plt.plot(n,exact(n),'--')
plt.plot(t,u)
plt.legend(['exact','Runge Kutta'])
plt.title('Runge Kutta vs exact')
plt.ylabel('y')
plt.axis([0,4,0,5])
plt.subplot(2,1,2)
plt.plot(n,exact(n),'--')
plt.plot(t1,u1,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['exact','Euler'])
plt.title('Exact vs Euler')
plt.axis([0,4,0,5])
plt.show()

u1,t1 = forEuler.solve(q)
u,t = rk4.solve(q)

plt.subplot(2,1,1)
plt.plot(n,exact(n),'--')
plt.plot(t,u)
plt.legend(['exact','Runge Kutta'])
plt.title('Runge Kutta vs exact')
plt.ylabel('y')
plt.axis([0,4,0,5])
plt.subplot(2,1,2)
plt.plot(n,exact(n),'--')
plt.plot(t1,u1,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['exact','Euler'])
plt.title('Exact vs Euler')
plt.axis([0,4,0,5])
plt.show()

"""
Ser at Runge Kutta 4 er en mye bedre tilnaerming enn Euler,
Runge Kutta har 100 punkter og er ganske naerme mens Euler blir naermere
forst etter 260 punkter. Lagt ved to plott som viser dette, 1 plott er 100 punkter
2 plott er 260 punkter

Terminal> python yx_ODE_FE_vs_RK4.py 
"""





