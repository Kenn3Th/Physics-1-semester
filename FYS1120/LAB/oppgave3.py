# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import functions as fx
import numpy as np

h= np.linspace(0,10,6)/1e2 + 0.0001
B= np.array([3., 1.807, 0.916, 0.696, 0.527, 0.492])/1e3

def B_func(h):
    '''
        Attempting to model the same data with a function, but doesn't appear to
        work too well unfortunately
    '''
    mu0= 4.*np.pi*1e-7
    a= 0.0375
    circumference= a*2.*np.pi
    N= 244
    length= circumference*N
    Js= 5./length
    t= .275
    return (mu0*Js/2.)*(((h+t)/((h+t)**2 + a**2))-(h/(np.sqrt(h**2 + a**2))))

f= fx.least_squares_functions((h, B), ['np.log(x)','1./x'])
x2= np.linspace(h[0], h[-1], 1000)
plt.xlim(h[0], h[-1])
plt.ylim(min(B)-0.2*min(B), 1.2*max(B))
plt.title('Magnetiske feltet $B$ som en funksjon av avstanden $h$ fra senteret av en spole', size= 20)
plt.xlabel('$h$ [m]', size= 15)
plt.ylabel('$B$ [T]', size= 15)
plt.plot(h, B, 'rx')
plt.plot(x2, f(x2))
plt.legend([u'Måleresultater','Interpolasjon'], prop={'size': 15})
plt.show()
