import sys

if len(sys.argv) < 2: #giving the programmer a msg if values is not inserted in the command line!
    print 'Provide a start velocity(m/s) and a time value(sec)! Only insert numbers!'
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
g = 9.81
q = float((2*v0)/g)

if t > 0 and t < q: #check if t is between 0 and (2*v0)/g
    k = y(v0,t)     
    print 'The ball is %.2f meters in the air' % k #if the the statement is true its printing the result
else:
    print 'Time value did not meet the requirements!' #printing msg if the statement is wrong
    exit() #ending the program

"""
Terminal> python ball_cml_tcheck.py
Provide a start velocity(m/s) and a time value(sec)! Only insert numbers!

Terminal>  python ball_cml_tcheck.py 6 2
Time value did not meet the requirements!

Terminal> python ball_cml_tcheck.py 7 1.2
The ball is 1.34 meters in the air
"""
