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

    r = k*(4/np.pi)

    plt.ion() #viktig a ha med nar plotet skal vises i en film
    plt.plot(r)
    plt.draw()
    plt.pause(1)
    

T = 2*np.pi
t = np.linspace(0.0, T, 200)
n = [1, 3, 20, 200, 2]
ft = np.array([f(t[i],T) for i in range(len(t))])

plt.plot(ft,'black', linewidth = 2.5)
plt.axis([-0.2, 201,-1.5, 1.5])        
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sinesum')

plt.legend(['F(t)','S(t;1)', 'S(t;3)','S(t;20)', 'S(t;200)'])    
plt.show()
