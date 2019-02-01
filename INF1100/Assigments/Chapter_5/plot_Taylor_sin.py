import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# formula ((-1)**j)*(x**(2*j+1)/factorial(2*j+1)
# a)

def S(x, n):
    s = 0.0
    for j in range(n+1):
        s = s + (-1)**j*(x**(2*j+1)/factorial(2*j+1.0))
        
    return s

# b)

x = np.linspace(0, 4*np.pi, 150)
n = [1,2,3,6,12]

plt.plot(x, np.sin(x), 'black', linewidth = 2)
for i in (n):
    b = S(x, i)
    plt.plot(x, b)
plt.axis([0, 4*np.pi, -1.5, 2])
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['sin(x)', 'S(x;1)', 'S(x;2)', 'S(x;3)', 'S(x;6)', 'S(x;12)'])
plt.title('Taylorpolynomet av grad n til sin(x)')
plt.show()

"""
Terminal:python plot_Taylor_sin.py
"""
