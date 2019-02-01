import numpy as np

"""
#a)
a[j] = -x**2/((2*j+1)*2*j)*a[j-1]
s[j] = s[j-1] + a[j-1]
"""
#b)

def sin_taylor(x,n):
    a = np.zeros(n+2)
    s = np.zeros(n+2)

    a[0] = x
    #s[0] = 0 trenger ikke denne pga s = np.zeros()

    for j in range(1, n+2):
        a[j] = -x**2/((2*j+1)*2*j)*a[j-1]
        s[j] = s[j-1] + a[j-1]

    return s[n+1], abs(a[n+1]) #abs = absolutt verdien

#print sin_taylor(np.pi/2, 40)

#c)

"""
n = 2
S = x - (x**3)/3! + (x**5)/5!)
"""
from math import factorial
def test_sin_Taylor():
    n = 2
    x = (3*np.pi)/2
    tol = 1e-10

    expected = x - (x**3)/factorial(3) + (x**5)/factorial(5)
    computed = sin_taylor(x,n)
    success = abs(expected - computed[0]) < tol
    msg = 'something went wrong'
    assert success, msg

test_sin_Taylor()

#d)

x = np.pi/2
for n in range(10):
    s = sin_taylor(x,n)
    print s[0]
