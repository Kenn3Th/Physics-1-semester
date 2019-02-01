#V(t) = folk som er vaksinert
#V'(t) = p*S #ODE

import SIR_class as sir, ODEsolver as ODE, matplotlib.pyplot as plt

class vaccination(sir.ProblemSIR):
    import ODEsolver as ODE
    def __init__(self, nu, beta, S0, I0, R0, T, V0, p):
        sir.ProblemSIR.__init__(self, nu, beta, S0, I0, R0, T)
        if isinstance(p, (float,int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p
        self.V0 = V0

    def __call__(self, u, t):
        S, I, R, V = u
        return [-self.beta(t)*S*I - self.p(t)*S, self.beta(t)*S*I - self.nu(t)*I,\
                self.nu(t)*I, self.p(t)*S]

    def initial_value(self):
        return self.S0, self.I0, self.R0, self.V0
    
if __name__ == '__main__':  #lager denne fordi jeg skal importere i et annet program
    dt = 0.5
    problem = vaccination(nu=0.1, beta=0.0005, S0=1500, I0=1, R0=0, T=60, V0=0, p=0.1)
    solver = ODE.RungeKutta4(problem)
    solver.set_initial_condition(problem.initial_value())
    y, x = solver.solve(problem.time_points(dt))
    S = y[:,0]; I = y[:,1]; R = y[:,2]; V = y[:,3]

    plt.plot(x,S,x,I,x,R,x,V)
    plt.legend(['Motagelig for sykdom', 'Smitta', 'Friske "meldt"','Vaksinert'])
    plt.axis([0,60,0,2000])
    plt.xlabel('Dager')
    plt.ylabel('Personer')
    plt.title('SIR model med Vaksinasjon')
    plt.show()

"""
I oppgave E.41 var max smittede oppe i ca 900 personer men med
vaksinasjon synker antall smittede til kun ca 50 personer,
det blir dermed ingen epidemi og sykdommen er kontrollert

Terminal> python SIRV.py
"""
