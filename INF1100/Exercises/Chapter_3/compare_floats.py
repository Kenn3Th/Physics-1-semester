a = 1/947.0*947
b = 1
if a != b:
    print 'Wrong result! a = %.16f b = %.16f' %(a, b)

tol = 1e-10

if abs(a - b) < tol:
    print 'Correct'
