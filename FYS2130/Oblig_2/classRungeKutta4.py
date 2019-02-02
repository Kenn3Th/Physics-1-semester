import numpy as np, matplotlib.pyplot as plt

class DrivenPendulum:

    def __init__(self,f0,omega_f,k,b,m):
        self.f0, self.omega, self.k, self.b, self.m = f0, omega_f, k, b, m

    
    def  __call__(self,x,v,t):
        a = self.f0*np.cos(self.omega*t) -self.b/self.m*v-self.k/self.m*x
        return a

class RungeKutta4:

    def __init__(self,f):
        self.f = f

    def __call__(self,x0,v0,t0,dt):
        a1 = self.f(x0,v0,t0)
        v1 = v0
        xHalv1 = x0 + v1 * dt/2.0
        vHalv1 = v0 + a1 * dt/2.0
        a2 = self.f(xHalv1,vHalv1,t0+dt/2.0)
        v2 = vHalv1
        xHalv2 = x0 + v2 * dt/2.0
        vHalv2 = v0 + a2 * dt/2.0
        a3 = self.f(xHalv2,vHalv2,t0+dt/2.0)
        v3 = vHalv2
        xEnd = x0 + v3 * dt
        vEnd = v0 + a3 * dt
        a4 = self.f(xEnd,vEnd,t0 + dt)
        v4 = vEnd
        aMid = 1.0/6.0 * (a1 + 2*a2 + 2*a3 + a4)
        vMid = 1.0/6.0 * (v1 + 2*v2 + 2*v3 + v4)
        xEnd = x0 + vMid * dt
        vEnd = v0 + aMid * dt
        return xEnd, vEnd
"""
def test_rk4():
    f = lambda x,v,t : 
    tRK4 = RungeKutta4(0.1,10.0,0.1)
    compx, compv = tRK4.rk4(0.1,0,0,0.3)
    expect1,expect2 = 0.029, 1.233
    tol = np.exp(-7) #grunnet avrunding i expect.
    success = abs((compx+compv)-(expect1+expect2)) < tol
    msg = 'FEIL!'
    assert success, msg
    
test_aks()
test_rk4()
"""
if __name__ == '__main__':

    #konstanter
    m = 0.1 #[kg]
    k = 10  #[N/m]
    b = 0.1 #[kg/s]
    N = 10000

    #arrays
    z = np.zeros(N)
    v = np.zeros(N)
    t = np.linspace(0, 10, N)

    #initial betingelser
    z[0] = 0.1     #[m]
    v[0] = 0       #[m/s]
    dt = t[1]-t[0] #tidssteg

    #iterasjoner i Runge-Kutta 4
    dp = DrivenPendulum(0,0,k,b,m)
    solver = RungeKutta4(dp)
    for i in range(N-1):
        z[i+1], v[i+1] = solver(z[i],v[i],t[i],dt)

    #analytisk losning
    A = 0.1
    omega = (np.sqrt(399)/2.0)
    #Funksjon for det analytiske uttrykket for z(t)
    def y(t):
        y = np.exp(-0.5*t)*A*np.cos(omega*t)
        return y
    an = np.zeros(N)
    an[0] = A
    for i in range(N-1):
        an[i+1] = y(t[i])


    
    #plott
    plt.plot(t,z)
    plt.title('Fjaer pendel')
    plt.xlabel('Tid[s]')
    plt.ylabel('Posisjon[m]')
    #plt.savefig('400.png')

    plt.plot(t,an)
    plt.legend(['RK4', 'analytisk'])
    #plt.savefig('AnalytiskmotRK4.png')
    plt.show()
