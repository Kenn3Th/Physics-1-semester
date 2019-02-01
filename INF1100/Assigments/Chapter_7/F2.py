"""
class = data + function
data: a, w
funktions: value(x)
"""

class F:
    def __init__(self,a,w):
        self.a = a
        self.w = w

    def __call__(self,x):
        from math import exp, sin
        return exp(-self.a*x)*sin(self.w*x)
    
    def value(self,x):
        from math import exp, sin
        return exp(-self.a*x)*sin(self.w*x)

    def __str__(self):
        return 'exp(-a*x)*sin(w*x)'

"""
Jeg brukte samme verdi som i boka saa fikk dermed samme resultat.
Legger ved en demo:
Terminal> python
>>> from F2 import F
>>> f = F(a=1.0, w=0.1)>>> from math import pi
>>> print f(x=pi)
0.013353835137
>>> f.a = 2
>>> print f(pi)
0.00057707154012
>>> print f
exp(-a*x)*sin(w*x)
"""
