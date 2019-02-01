class rectangle:
    
    def __init__(self, llc, w, h):
        self.llcorner, self.W, self.H = llc, w, h

    def area(self):
        return self.W * self.H

    def perimeter(self):
        return 2*self.W + 2*self.H

"""
Triangle
formula 1/2|x2y3 - x3y2 - x1y3 + x3y1 + x1y2 - x2y1|
"""

class triangle:

    def __init__(self, vert0, vert1, vert2):
        self.A, self.B, self.C = vert0, vert1, vert2
    
    def area(self):
        a = {1: self.A, 2: self.B, 3: self.C} #lagrer vektorene i en dictionary
        return 0.5*abs(a[2][0]*a[3][1]-a[3][0]*a[2][1]-a[1][0]*a[3][1] + \
                       a[3][0]*a[1][1]+a[1][0]*a[2][1] -a[2][0]*a[1][1])

    def perimeter(self):
        import numpy as np #det er enklere med array naar jeg regner med vektorer
        A = np.array(self.A); B = np.array(self.B); C = np.array(self.C)
        a = A-B; b = B-C; c = A-C
        return np.sqrt(sum(a**2)) + np.sqrt(sum(b**2)) + np.sqrt(sum(c**2))

def test_rectangle():
    q = rectangle((3,2), 6, 2)
    comp1, comp2 = q.area(), q.perimeter()
    ex1, ex2 = 12, 16
    tol = 1E-14
    success = abs(comp1-ex1) < tol and abs(comp2-ex2) < tol
    msg = 'there is a bug in rectangle'
    assert success, msg

def test_triangle():
    z = triangle((1,1), (4,1), (1,5))
    comp1, comp2 = z.area(), z.perimeter()
    ex1, ex2 = 6, 12
    tol = 1E-14
    success = abs(comp1-ex1) < tol and abs(comp2-ex2) < tol
    msg = 'somthing is wrong with triangle function!!'
    assert success, msg
    
test_rectangle()
test_triangle()

a = rectangle((0,0), 3, 5)
print '''A rectangle with width %g ang hight %g has an area = %g.
The left corner of the rectangle is located at %s''' % (a.W, a.H, a.area(), a.llcorner)

print

r = triangle((2,3), (6,4), (4,7))
print '''A triangle with the cordinates %s, %s, %s,
has an area = %g a perimiter = %g''' % (r.A, r.B, r.C, r.area(), r.perimeter())

"""
Terminal >python geometric_shapes.py 
A rectangle with width 3 ang hight 5 has an area = 15.
The left corner of the rectangle is located at (0, 0)

A triangle with the cordinates (2, 3), (6, 4), (4, 7),
has an area = 7 a perimiter = 12.2008
"""
