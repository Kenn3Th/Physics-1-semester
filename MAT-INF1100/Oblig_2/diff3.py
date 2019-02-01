import numpy as np

k = [0,1,2,3,4,5]
n = 5
x = np.zeros(len(k))
t = np.zeros(len(k))

for i in range(1,n+1):
    h = 0.4
    xtmp = x[i-1] + (h/2)*(1-x[i-1]**2)
    x[i] = x[i-1] + h*(1-xtmp**2)
    t[i] = (i)*h
