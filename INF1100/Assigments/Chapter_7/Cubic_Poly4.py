# Y = c0 + c1x
class Line(object):
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1

    def __call__(self,x):
        print 'Line', self.c0 + self.c1*x
        return self.c0 + self.c1*x

    def table(self, L, R,n):
        """return a table with n points for L <= x <= R."""
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s
    
#Parabola Y = c0 + c1x + c2x^2
class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2

    def __call__(self,x):
        print 'Parabola', Line.__call__(self, x) + self.c2*x**2
        return Line.__call__(self, x) + self.c2*x**2

#Cubic Y = c3x^3 + c2x^2 + c1x + c0
class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3

    def __call__(self,x):
        print 'Cubic', Parabola.__call__(self,x) + self.c3*x**3
        return Parabola.__call__(self,x) + self.c3*x**3

#Poly4 Y = c4x^4 + c3x^3 + c2x^2 + c1x + c0
class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self,x):
        print 'poly', Cubic.__call__(self,x) + self.c4*x**4
        return Cubic.__call__(self,x) + self.c4*x**4

pol = Poly4(1, 1, 2, 2, 10)
pol(4)

"""
Terminal> python Cubic_Poly4.py 
poly Cubic Parabola Line 5
37
Line 5
165
Parabola Line 5
37
Line 5
2725
Cubic Parabola Line 5
37
Line 5
165
Parabola Line 5
37
Line 5
"""
