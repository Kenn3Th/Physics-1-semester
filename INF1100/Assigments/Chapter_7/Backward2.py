class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

class Forward1(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x*h) - f(x))/h

class Backward1(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Backward2(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x-2*h) - 4*f(x-h) + 3*f(x))/(2*h)

from math import exp
k = 14
t = 0
neg_e = lambda t: -exp(t)
exct_dt = -1
for i in range(k+1):
    h = 2**(-i)
    gt2 = Backward2(neg_e, h)
    gt = Backward1(neg_e, h)
    dif2 = gt2(0) - exct_dt
    dif = gt(0) - exct_dt
    print '--------------------------------------------------------------'
    print "|k = %2.d,| g'(t) = -1,| Backward1 = %-8.5g,| Difference = %-6.5g" %(i,gt(0), dif)
    print "|k = %2.d,| g'(t) = -1,| Backward2 = %-8.5g,| Difference = %-6.5g" %(i,gt2(0), dif2)
    
"""
Terminal> python Backward2.py 
--------------------------------------------------------------
|k =   ,| g'(t) = -1,| Backward1 = -0.63212,| Difference = 0.36788
|k =   ,| g'(t) = -1,| Backward2 = -0.83191,| Difference = 0.16809
--------------------------------------------------------------
|k =  1,| g'(t) = -1,| Backward1 = -0.78694,| Difference = 0.21306
|k =  1,| g'(t) = -1,| Backward2 = -0.94176,| Difference = 0.058243
--------------------------------------------------------------
|k =  2,| g'(t) = -1,| Backward1 = -0.8848 ,| Difference = 0.1152
|k =  2,| g'(t) = -1,| Backward2 = -0.98266,| Difference = 0.017345
--------------------------------------------------------------
|k =  3,| g'(t) = -1,| Backward1 = -0.94002,| Difference = 0.059975
|k =  3,| g'(t) = -1,| Backward2 = -0.99525,| Difference = 0.0047473
--------------------------------------------------------------
|k =  4,| g'(t) = -1,| Backward1 = -0.96939,| Difference = 0.030609
|k =  4,| g'(t) = -1,| Backward2 = -0.99876,| Difference = 0.0012428
--------------------------------------------------------------
|k =  5,| g'(t) = -1,| Backward1 = -0.98454,| Difference = 0.015464
|k =  5,| g'(t) = -1,| Backward2 = -0.99968,| Difference = 0.000318
--------------------------------------------------------------
|k =  6,| g'(t) = -1,| Backward1 = -0.99223,| Difference = 0.007772
|k =  6,| g'(t) = -1,| Backward2 = -0.99992,| Difference = 8.0433e-05
--------------------------------------------------------------
|k =  7,| g'(t) = -1,| Backward1 = -0.9961 ,| Difference = 0.0038961
|k =  7,| g'(t) = -1,| Backward2 = -0.99998,| Difference = 2.0226e-05
--------------------------------------------------------------
|k =  8,| g'(t) = -1,| Backward1 = -0.99805,| Difference = 0.0019506
|k =  8,| g'(t) = -1,| Backward2 = -0.99999,| Difference = 5.0714e-06
--------------------------------------------------------------
|k =  9,| g'(t) = -1,| Backward1 = -0.99902,| Difference = 0.00097593
|k =  9,| g'(t) = -1,| Backward2 = -1      ,| Difference = 1.2697e-06
--------------------------------------------------------------
|k = 10,| g'(t) = -1,| Backward1 = -0.99951,| Difference = 0.00048812
|k = 10,| g'(t) = -1,| Backward2 = -1      ,| Difference = 3.1766e-07
--------------------------------------------------------------
|k = 11,| g'(t) = -1,| Backward1 = -0.99976,| Difference = 0.0002441
|k = 11,| g'(t) = -1,| Backward2 = -1      ,| Difference = 7.9444e-08
--------------------------------------------------------------
|k = 12,| g'(t) = -1,| Backward1 = -0.99988,| Difference = 0.00012206
|k = 12,| g'(t) = -1,| Backward2 = -1      ,| Difference = 1.9864e-08
--------------------------------------------------------------
|k = 13,| g'(t) = -1,| Backward1 = -0.99994,| Difference = 6.1033e-05
|k = 13,| g'(t) = -1,| Backward2 = -1      ,| Difference = 4.9658e-09
--------------------------------------------------------------
|k = 14,| g'(t) = -1,| Backward1 = -0.99997,| Difference = 3.0517e-05
|k = 14,| g'(t) = -1,| Backward2 = -1      ,| Difference = 1.2442e-09
"""
