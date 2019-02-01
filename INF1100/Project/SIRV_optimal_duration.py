import SIRV, ODEsolver as ODE, matplotlib.pyplot as plt, numpy as np

dt = 0.5
V = [range(31)]
def gamma(t):
    p = 0
    if 6 <= t <= (6+V):
        p = 0.1
    else:
        p = 0
    return p

problem = SIRV.vaccination(nu=0.1, beta=0.0005, S0=1500, I0=1, R0=0,\
                           T=10, V0=0, p=gamma)
solver = ODE.RungeKutta4(problem)
solver.set_initial_condition(problem.initial_value())
y, x = solver.solve(problem.time_points(dt))
S = y[:,0]; I = y[:,1]; R = y[:,2]; V = y[:,3]

plt.plot(x,S,x,I,x,R,x,V) 
plt.legend(['Motagelig for sykdom', 'Smitta', 'Friske "meldt"','Vaksinert'])
plt.axis([0,31,0,2000])
plt.xlabel('Dager')
plt.ylabel('Personer')
plt.title('SIR model med Vaksinering etter 6 dager')
plt.show()
