import sys

def y(v0, t):              #function
    g = 9.81               #gravity on earth
    Fy = v0*t - 0.5*g*t**2 #formula
    return Fy

def test_y():  #test if the function is working
    computed = y(2, 1)
    expected = -2.905
    tol = 1e-10
    success = (computed - expected) < tol
    msg = 'something is wrong'
    assert success, msg
test_y()       #calling the test

if len(sys.argv) < 2:
    v0 = raw_input('initial velocity? '); v0 = float(v0)
    t = raw_input('time? '); t = float(t) 
    b = y(v0, t)                     #calling the function
    print b
else:
    v0 = sys.argv[1]; v0 = float(v0) #fetching the first number from the command line
    t = sys.argv[2]; t = float(t)    #fetching the second number from the command line
    h = y(v0, t)                     #calling the function
    print h

"""
Terminal> python ball_cml_qa.py
initial velocity? 4
time? 0.2
0.6038

or

Terminal> python ball_cml_qa.py 4 0.2
0.6038
"""
