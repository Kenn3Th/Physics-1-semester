class ProblemSIR():
    def __init__(self, nu, beta, S0, I0, R0, T):
        if isinstance(nu, (float,int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu
        if isinstance(beta, (float,int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        self.S0, self.I0, self.R0, self.T = S0, I0, R0, T
         
    def __call__(self, u, t):
        S, I, R = u
        return [-self.beta(t)*S*I, self.beta(t)*S*I - self.nu(t)*I,\
                self.nu(t)*I]
                
    def initial_value(self):
        return self.S0, self.I0, self.R0
    
    def time_points(self,dt):
        import numpy as np
        self.dt = dt
        t = np.linspace(0,self.T, self.T/float(self.dt))
        return t

class SolverSIR():
    import ODEsolver as ODE
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ODE.RungeKutta4):
        import numpy as np
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u , self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]

    def plot(self):
        import matplotlib.pyplot as plt
        S, I, R, t = self.S, self.I, self.R, self.t
        plt.plot(t,S,t,I,t,R)
        plt.legend(['Motagelig for sykdom', 'Smitta', 'Friske "meldt"'])
        plt.axis([0,60,0,2000])
        plt.xlabel('Dager')
        plt.ylabel('Personer')
        plt.title('SolverSIR')
        plt.show()

if __name__ == '__main__': #lager denne fordi jeg skal importere i et annet program
    import ODEsolver as ODE, matplotlib.pyplot as plt
    
    def betta(t): #funksjon for beta
        betta = 0
        if t<=12:
            betta = 0.0005
        else:
            betta = 0.0001
        return betta

    dt = 0.5 #steg lengde
    problem = ProblemSIR(nu=0.1, beta=betta, S0=1500, I0=1, R0=0, T=60)
    solver = ODE.RungeKutta4(problem)
    solver.set_initial_condition(problem.initial_value())
    y, x = solver.solve(problem.time_points(dt))
    S = y[:,0]; I = y[:,1]; R = y[:,2]
    
    #plott for ProblemSIR
    plt.plot(x,S,x,I,x,R)
    plt.legend(['Motagelig for sykdom', 'Smitta', 'Friske "meldt"'])
    plt.axis([0,60,0,2000])
    plt.xlabel('Dager')
    plt.ylabel('Personer')
    plt.title('ProblemSIR')
    plt.show()

    #plott for SolverSIR
    prob = SolverSIR(problem,dt)
    prob.solve()
    prob.plot()

"""
Naar jeg sammenligner grafene fra ProblemSIR, SolverSIR og SIR.py
er det forskjell paa de smitta.
I SIR.py er max smitta oppe i ca 900 personer paa en gang.
Det er en veldig liten forskjell paa grafene fra ProblemSIR og SolverSIR
disse har max smitta paa ca 750 personer paa engang.
Naar vi ser paa antall motagelig for smitte ser vi at ikke alle har blitt smittet
i ProblemSIR og SolverSIR. Det er igjen litt under 200 som ikke er blitt smittet.

jeg bruker false i terminate funksjonen min pga av dette staar i ODEsolveren:
Compute solution u for t values in the list/array
time_points, as long as terminate(u,t,step_no) is False.
terminate(u,t,step_no) is a user-given function
returning True or False. By default, a terminate
function which always returns False is used.

Terminal> python SIR_class.py
"""
