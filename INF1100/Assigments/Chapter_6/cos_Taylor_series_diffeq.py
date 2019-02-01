"""
formula: (-1)**n*(x**2n/2n!)
#a)
a[j] = -x**2/(2.0*j*(2*j-1))*a[j-1]
s[j] = s[j-1] + a[j-1]

"""
#b)

import numpy as np
from math import factorial

def cos_taylor(x,n):
    a = np.zeros(n+2)
    s = np.zeros(n+2)

    a[0] = 1.
    s[0] = 0

    for j in range(1, n+2):
        a[j] = -x**2/(2.0*j*(2*j-1))*a[j-1]
        s[j] = s[j-1] + a[j-1]

    return s[n+1], abs(a[n+1]) #abs = absolutt verdien
#c)
def test_cos_Taylor():
    n = 3
    x = (3*np.pi)/2
    tol = 1e-10

    expected = 1 - (x**2)/factorial(2) + (x**4)/factorial(4) - (x**6)/factorial(6)
    computed = cos_taylor(x,n)
    success = abs(expected - computed[0]) < tol
    msg = 'something went wrong'
    assert success, msg

test_cos_Taylor()

x = np.pi

for n in range(10):
    s = cos_taylor(x,n)
    print s[0]
    
"""
Terminal>  python cos_Taylor_series_diffeq.py 
1.0
-3.93480220054
0.123909925872
-1.21135284298
-0.976022212624
-1.00182910401
-0.999899529704
-1.00000416781
-0.99999986474
-1.00000000353
"""
