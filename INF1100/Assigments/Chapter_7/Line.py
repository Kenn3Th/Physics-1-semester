class Line:

    def __init__(self,p1,p2):
        self.p1, self.p2 = p1,p2

    def value(self):
        x0, y0 = self.p1[0], self.p1[1]  
        x1, y1 = self.p2[0], self.p2[1] 
        a = (y1 - y0)/float(x1-x0); b = y0*a*x0
        return b

def test_Line():
    comp = Line((1.5,3.4), (4,1.1)).value()
    expect = -4.692
    tol = 1e-15
    success = abs(comp - expect) < tol
    msg = 'it did not go as planned'
    assert success, msg

test_Line()

print Line((3, 5.5), (5, 6.5)).value()

"""
Terminal> python Line.py
8.25
"""
