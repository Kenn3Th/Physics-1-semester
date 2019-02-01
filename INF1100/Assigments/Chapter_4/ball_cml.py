import sys

if len(sys.argv) < 2: #gives a msg if values is not inserted in the command line!
    print 'Provide a start velocity and a time value! Only insert numbers!'
    exit()

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

v0 = sys.argv[1]; v0 = float(v0) #fetching the first number
t = sys.argv[2]; t = float(t)    #fetching the second number

h = y(v0, t)   #calling the function
print h 

"""
Terminal> python ball_cml.py
Provide a start velocity and a time value! And only insert numbers!

Terminal> python ball_cml.py 10 1.3
4.71055
"""
