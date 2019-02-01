# equation ax**2 + bx + c = 0
# abc formula x = (-b +- sqrt(b**2 - (4*a*c)))/2*a

from cmath import sqrt as csqrt # roots for complex numbers
from math import sqrt           # roots for regular numbers

def roots(a, b, c):
    if (b**2 - (4*a*c)) < 0: # if this is true its complex number
        x1 = (-b + csqrt(b**2 - (4*a*c)))/2*a
        x2 = (-b - csqrt(b**2 - (4*a*c)))/2*a
    else:                    # if it is false it is a regular number
        x1 = (-b + sqrt(b**2 - (4*a*c)))/2*a
        x2 = (-b - sqrt(b**2 - (4*a*c)))/2*a
    return x1, x2

def test_roots_complex(): #test function for complex roots
    x1,x2 = roots(1, -2, 5)
    expected1, expected2 = (1+2j), (1-2j)
    tol = 1e-10
    success = abs((x1 + x2) - (expected1 + expected2)) < tol
    if not success:
        print 'FAIL!!'

def test_roots_floats(): #test function for regular roots
    x1,x2 = roots(1, -4, 3)
    expect1, expect2 = (3.0), (1.0)
    success = abs((x1 + x2) - (expect1 + expect2)) < 1e-10
    msg = 'Not right!'
    assert success, msg

test_roots_complex()
test_roots_floats()

y = roots(1,-2, 5)
x = roots(1, -4, 3)
print x,y

"""
Terminal>python roots_quadratic.py 
(3.0, 1.0) ((1+2j), (1-2j))
"""
