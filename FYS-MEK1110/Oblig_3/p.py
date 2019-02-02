from pylab import*

Au = 149597870691 #meter
time = 10
dt = 0.001
n = int(round(time/dt))
array = zeros(len(t))


"""
#Euler-Cromer
for i in range(n-1):
    F = -k*x[i]
    a[i] = F/m
    v0[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt
    t[i+1] = t[i] + dt
"""
print array
