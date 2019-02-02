import numpy as np, matplotlib.pyplot as plt, scipy as sp
from classRungeKutta4 import*

#konstanter
m = 0.1
k = 10.0
b = 0.04
F0 = 0.1
N = 10**3
#arrays
z = np.zeros(N)
v = np.zeros(N)
t = np.linspace(0, 50, N)

#initial betingelser
z[0] = 0     #[m]
v[0] = 0       #[m/s]
dt = t[1]-t[0] #tidssteg
omegaF0 = np.sqrt((k/m)-(b**2/(2*m**2)))
omega = np.sqrt(k/m)

omegaFs = np.linspace(0.5,1.5,300)*omegaF0
responses = np.zeros(len(omegaFs))


for j,omegaF in enumerate(omegaFs):        
    drivenpendulum = DrivenPendulum(F0,omegaF,k,b,m)
    solver = RungeKutta4(drivenpendulum)    

    #iterasjoner i Runge-Kutta 4
    for i in range(N-1):
        z[i+1], v[i+1] = solver(z[i],v[i],t[i],dt)
    siste = z[-300:-1]
    z_ = np.mean(siste*siste)
    Amplitude = 2*z_
    responses[j] = np.sqrt(Amplitude)

    #plott
    plt.plot(t,z)
    plt.xlabel('Tid[s]')
    plt.ylabel('Utslag[m]$')

plt.figure()
plt.plot(omegaFs,responses)
plt.xlabel('$\omega_F$')
plt.ylabel('Amplitude/respons')
plt.title('Frekvensrespons')
plt.show()

