from numpy import *
import matplotlib.pyplot as plt
from math import factorial

def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):

    x = linspace(xmin, xmax, n)
    s = zeros_like(x)
    s_ref = exact(x)

    plt.ion() #viktig a ha med nar plotet skal vises i en film
    plt.plot(x, s_ref)

    lines = plt.plot(x,s)

    plt.axis([xmin, xmax, ymin, ymax])

    for k in range(M,N+1):
        s = s + fk(x, k)
        lines[0].set_ydata(s)
        plt.draw()
        plt.pause(0.25)
        

def taylor_sin(x, k):
    return (-1.0)**k*x**(2*k+1)/factorial(2*k+1)

def exp_inv(x):
    return exp(-x)

def taylor_exp_inv(x,k):
    return (-x)**k/factorial(k)

#animate_series(taylor_sin,0,20,0,13*pi,-2,2,100,sin)
animate_series(taylor_exp_inv,0,30,0,15,-0.5,1.4,100,exp_inv)
