import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi

# a)
def sequence_a(N):
    index_set = range(N+1)
    a = np.zeros(len(index_set))

    for n in index_set:
        a[n] = (7+1.0/(n+1))/(3-1.0/(n+1)**2)
    return a

#print sequence_a(100)

#b)
def sequence_b(N):
    index_set = range(N+1)
    D = np.zeros(len(index_set))

    for n in index_set:
        D[n] = sin(2**-n)/2**-n

    return D

#print sequence_b(100)

#c)

def sequence_c(f, x, N):
    index_set = range(N+1)
    D = np.zeros(len(index_set))

    for n in index_set:
        h = 2**(-n)
        D[n] = (f(x+h) -f(x))/h

    return D

Dn = sequence_c(sin, pi, 80)

plt.plot(Dn,'bo')
plt.axis([0, 80, -1.5, 1.5])
plt.show()
