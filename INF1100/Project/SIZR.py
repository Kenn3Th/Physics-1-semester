"""
S = sigma-betta*S*Z-ds*S
I = betta*S*Z-p*I-delta*I
Z = p*I - alfa*S*Z
R = ds*S + delta*I + alfa*S*Z
"""

class ProblemSIR():
    def __init__(self, sigma, betta, delta, alfa, S0, Z0, I0, R0, T, p):
        if isinstance(nu, (float,int)):
            self.sigma = lambda t: sigma
        elif callable(sigma):
            self.sigma = sigma
        if isinstance(beta, (float,int)):
            self.betta = lambda t: betta
        elif callable(betta):
            self.betta = betta
        self.delta, self.alfa = delta, alfa
        self.S0, self.Z0, self.I0, self.R0, self.T, self.p = S0, Z0, I0, R0, T, p
         
    def __call__(self, u, t):
        S, Z, I, R = u
        ds = 
        return [
            self.sigma(t) -self.betta(t)*S*Z - ds*S,
            self.betta(t)*S*Z - self.p*I - self.delta*I,
            self.p*I - self.alfa*S*Z,
            ds*S + self.delta*I + self.alfa*S*Z
            ]
                
    def initial_value(self):
        return self.S0, self.Z0, self.I0, self.R0
    
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
        ic = [self.problem.S0, self.problem.Z0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u , self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]

    def plot(self):
        import matplotlib.pyplot as plt
        S, Z, I, R, t = self.S, self.Z, self.I, self.R, self.t
        plt.plot(t,S,t,Z,t,I,t,R)
        plt.legend(['Mennesker', 'Zombie' 'Smitta', 'Død'])
        plt.xlabel('Timer')
        plt.ylabel('Individer')
        plt.title('ZOMBIE')
        plt.show()
