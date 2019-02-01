from math import sqrt

x = [1, (1 - sqrt(2))]

for i in range(2,100+1):
    value = 2*(float(x[-1])) + float(x[-2])
    x.append(value)

def xn(n):
    return (1 - sqrt(2))**n

n = 100
for i in range(n+1):
    u = xn(i)
    b = x[i]
    w = u - b
    print 'x%g General solution = %12g  |  Computed solution = %12g  |  Avvik = %g' %(i, u, b, w)

