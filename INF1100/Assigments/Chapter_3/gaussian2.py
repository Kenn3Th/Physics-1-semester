#formula (1/sqrt(2*pi)*s)*exp[-0.5*((x-m)/s)**2]

from math import sqrt, pi, exp

def gauss(x, m=0, s=1):
    return 1.0/(sqrt(2*pi)*s)*exp(-0.5*((x-m)/s)**2)

n = 10; m = 5.0; s = 1.0
start = m - 5*s
stop = m + 5*s
step = float(start - stop)/n

X = []
Fx =[]

for x in range(n+1):
    X.append(x)
    fx = gauss(x, m, s)
    Fx.append(fx)
    x += step

for i, j in zip(X, Fx):
    print 'x = %-4.1f f(x) = %-4.6f' %(i, j)
    
"""
Terminal>python gaussian2.py 
x = 0.0  f(x) = 0.000001
x = 1.0  f(x) = 0.000134
x = 2.0  f(x) = 0.004432
x = 3.0  f(x) = 0.053991
x = 4.0  f(x) = 0.241971
x = 5.0  f(x) = 0.398942
x = 6.0  f(x) = 0.241971
x = 7.0  f(x) = 0.053991
x = 8.0  f(x) = 0.004432
x = 9.0  f(x) = 0.000134
x = 10.0 f(x) = 0.000001
"""
