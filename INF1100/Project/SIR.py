"""
S(t) = folk som kan bli sjuke
I(t) = folk som er smitta
R(t) = folk som har hatt sykdommen og er naa imun
dt = tids-intervall intervall

S(t+dt) = S(t) - beta*S*I*dt
S'(t) = - beta*S*I #ODE

I(t+dt) = I(t) + beta*S*I*dt - v*I*dt
I'(t) = beta*S(t)*I(t) - v*I #ODE

R(t+dt) = R(t) + V*I*dt
R'(t) = v*I #ODE
"""
import numpy as np, matplotlib.pyplot as plt, ODEsolver as ODE, sys

So = 1500; Io = 1; Ro = 0 #initial verdier
inv = [So,Io,Ro]          #liste av initial verdier
dt = 0.5                  #steg lengde
beta = 0.0005
v = 0.1                   #sannsynlighet for aa bli frisk per steg lengde
T = 60                    #dager
n = T/dt                  #Nr for steg lengder i time_point
time_point = np.linspace(0,60,n+1)

#ODE funksjons
def ODEfunk(inv, t):
    y = np.zeros((3))
    P = inv
    y[0] = - beta*P[0]*P[1] 
    y[1] = beta*P[0]*P[1] - v*P[1]
    y[2] = v*P[1]
    return y
tol = 1E-12
terminate = lambda u,t,k: False if np.abs(np.sum(u[k] - u[0])) < tol else True

Res = ODE.RungeKutta4(ODEfunk)
Res.set_initial_condition(inv)
y,x = Res.solve(time_point,terminate)
S = y[:,0]; I = y[:,1]; R = y[:,2]

plt.plot(x,S,x,I,x,R)
plt.legend(['Motagelig for sykdom', 'Smitta', 'Friske "meldt"'])
plt.axis([0,60,0,2000])
plt.xlabel('Dager')
plt.ylabel('Personer')
plt.title('Enkel SIR modell')
plt.show()


"""
Naar jeg ser paa de forskjellige grafene jeg faar av a endre beta
kan jeg konkludere med at en beta paa 0.0001 saa blir det
ingen epedemi.

Har hentet inpirsajon fra nettet, legger ved en kilde liste.
Kilde liste:
http://chengjunwang.com/en/2013/08/learn-basic-epidemic-models-with-python/

Terminal> python SIR.py 
"""
