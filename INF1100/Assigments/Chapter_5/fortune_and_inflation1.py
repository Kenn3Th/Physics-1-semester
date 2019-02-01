import numpy as np
import matplotlib.pyplot as plt

"""
differens ligning
x0 = F ; c0 = ((p*q)/1E*4)*F
x[n] = x[n-1] + (p/100)*x[n-1] - c[n-1]
c[n] = c[n-1] + (1/100)*c[n-1]
"""

F = 4     #fortune
p = 27.0   #annual interest of percent
q = 5.0  #interest of the first year
n = 10    # years

x = np.zeros(n+1)
c = np.zeros(n+1)
x[0] = F
c[0] = ((p*q)/1e4)*F

for i in xrange(1,n+1):
    c[i] = c[i-1] + (1/100)*c[i-1]
    x[i] = x[i-1] + (p/100)*x[i-1] - c[i-1]
    

plt.plot(x, '.-.-.')
plt.xlabel('years')
plt.ylabel('f(x)')
plt.title('Fortune')
plt.legend(['f(x) = %.2f' % (x[-1])])
plt.show()

"""
Terminal>python fortune_and_inflation1.py
"""
