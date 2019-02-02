import functions as fx
import matplotlib.pyplot as plt
import numpy as np

B= np.array([18., 66., 114, 164., 218., 272.])/1e3
Vh= np.array([4.5, 14., 22., 31., 40., 50.])/1e3

f= fx.least_squares_functions((B, Vh), 'x')
x2= np.linspace(B[0], B[-1], 1000)
plt.plot(B, Vh, 'rx')
plt.plot(x2, f(x2))
plt.xlabel('$B$ [T]', size=15)
plt.ylabel('$V_h$ [V]', size=15)
plt.xlim(B[0], B[-1])
plt.legend([u'Maaleresultater','Interpolasjon'], prop={'size': 15})
plt.title('Hall spenning $V_h$ som en funksjon av magnetiske feltet $B$', size=20)
a= (f(x2[-1])-f(x2[0]))/(x2[-1]- x2[0])
print('Stigningstall:%g'%(a))
plt.show()

'''1.2'''
d= 1e-3
I= .03
Rh= a*(d/I)
print(Rh) #Rh

N= 1./(Rh*1.6e-19)
print(N)

b= 0.01
d= 0.001
q= 1.6e-19
I= 0.03

print(I/(b*d*N*q))
