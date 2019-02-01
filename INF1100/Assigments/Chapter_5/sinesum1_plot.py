import numpy as np
import matplotlib.pyplot as plt

def f(t, T):

    if 0 < t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2 < t < T:
        return -1
        
def S(t,n,T):
    k = 0
    for i in range(1,n+1):
        k += 1.0/(2*i - 1)*np.sin((2*(2*i - 1)*np.pi*t)/T)
    return k*(4/np.pi)

T = 2*np.pi
t = np.linspace(0.0, T, 200)
n = [1, 3, 20, 200]
ft = np.array([f(t[i],T) for i in range(len(t))])

plt.plot(t, ft,'black', linewidth = 2)     
plt.xlabel('t')
plt.ylabel('f(t)/S(t;n)')
plt.title('Sinesum')
plt.legend(['F(t)'])
for i in (n):
    q = S(t,i,T)
    plt.plot(t,q)
plt.axis([-0.2, 6.5,-1.5, 1.5])   
plt.legend(['F(t)','S(t;1)', 'S(t;3)','S(t;20)', 'S(t;200)'])    
plt.show()

"""
Terminal> python sinesum1_plot.py
"""
