#formula v(r)= (Bet/2*gam)**(1/n) *(n/(n + 1)*(R**(1+1/n)-r**(1+1/n))

from numpy import linspace
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt

def v(r, n):
    R = 1; Bet = 0.02; gam = 0.02
    return ((Bet/2*gam)**(1./n))*(n/(n + 1.))*(R**(1+1./n) - r**(1+1./n))

#r elemnt [0, R]
R = 1
Bet = 0.02
gam = 0.02

n = 0.1
r_min = 0

r = linspace(r_min, R, 100)

for n in linspace(1, 0.1, 10):
    plt.plot(r, v(r, n) / v(0, n))
    plt.xlabel('radius')
    plt.ylabel('velocity')
    plt.title('Velocity profile: n = %1.2f' % n)
    
plot(r, v(r,n))
show()
