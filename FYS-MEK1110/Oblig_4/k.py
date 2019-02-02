from pylab import*

#Funksjoner
def f(x,y): #F_f = kraft som blir tilfort av fotoner
    if abs(x) >= X0:
        return 0
    else:
        return -alp*y
def F(x):  #F_m = den magnetiske kraften
    if abs(x) >= X0:
        return 0
    elif 0 > x > -X0:
        return U/X0
    else:
        return -U/X0
    
#initialverdier
U = 150.0; m = 23.0; X0 = 2.0; alp = 39.48
dt = 1E-5 ; time = 5.0

#Euler-cromer
n = int(round(time/dt))
t = linspace(0,5,n)
xi = zeros(n)
v = zeros(n)
a = zeros(n)
v[0] = 8; xi[0] = -5
for i in range(n-1):
    a[i] = (F(xi[i]) + f(xi[i],v[i]))/m
    v[i+1] = v[i] + a[i]*dt
    xi[i+1] = xi[i] + v[i+1]*dt
