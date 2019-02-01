"""
function:
f(x;a,b,c) = ax**2 +bx +c)

formula:
(-b +-sqrt(b**2 -(4*a*c)))/2
"""
import numpy as np
import cmath as cm

class quadratic:
    
    def __init__(self, a, b, c):
        self._a, self._b, self._c = a, b, c

    def roots(self):
        if self._b**2 > (4*self._a*self._c):
            r1 = (-self._b + np.sqrt(self._b**2 - (4*self._a*self._c)))/2*self._a
            r2 = (-self._b - np.sqrt(self._b**2 - (4*self._a*self._c)))/2*self._a
            return r1, r2
        elif self._b**2 == (4*self._a*self._c):
            return -self._b/2*self._a
        else:
            cr1 = (-self._b + cm.sqrt(self._b**2 - (4*self._a*self._c)))/2*self._a
            cr2 = (-self._b - cm.sqrt(self._b**2 - (4*self._a*self._c)))/2*self._a
            return cr1, cr2

    def value(self,x):
       return self._a*x**2 + self._b*x + self._c

    def table(self, L, R, n):
        self._L, self._R, self._n = L, R, n
        s = np.linspace(self._L, self._R, self._n)
        for i in range(len(s)+1):
            f = self._a*i**2 + self._b*i + self._c
            print 'x = %g f(x) = %g' %(i, f) 


def test_value():
    q = quadratic(2, -2, -2)
    comp = q.value(4)
    expect = 22
    tol = 1e-14
    success = abs(comp - expect) < tol
    msg = 'somthing is not right'
    assert success, msg

def test_roots():
    q = quadratic(1, -3, 2)
    comp1, comp2 = q.roots()
    exp1, exp2 = 2, 1
    tol = 1e-14
    success = ((comp1 + comp2)-(exp1+exp2)) < tol
    msg = 'I did not go as planned!!'
    assert success, msg

test_value()
test_roots()

                    
q = quadratic(3, -12, 4)

print 'value'
print q.value(4)
print'-----------------'
print 'table'
q.table(1,10,10)
print'-----------------'
print 'roots'
print q.roots()
print'-----------------'



"""
Terminal >python Quadratic.py 
value
4
-----------------
table
x = 0 f(x) = 4
x = 1 f(x) = -5
x = 2 f(x) = -8
x = 3 f(x) = -5
x = 4 f(x) = 4
x = 5 f(x) = 19
x = 6 f(x) = 40
x = 7 f(x) = 67
x = 8 f(x) = 100
x = 9 f(x) = 139
x = 10 f(x) = 184
-----------------
roots
(32.696938456699066, 3.3030615433009327)
-----------------

Demo av bruk av Quadratic som module:

Terminal> python
>>> from Quadratic import quadratic
>>> quadratic(1,-3,2).roots()
(2.0, 1.0)
>>> quadratic(2,4,2).value(3)
32
>>> quadratic(1,3,-2).table(1,5,5)
x = 0 f(x) = -2
x = 1 f(x) = 2
x = 2 f(x) = 8
x = 3 f(x) = 16
x = 4 f(x) = 26
x = 5 f(x) = 38

"""
