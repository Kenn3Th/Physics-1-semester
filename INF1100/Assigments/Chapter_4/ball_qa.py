
print '''
Only insert numbers
'''

def y(v0, t):
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

v0 = raw_input('What is the start velocity (m/s)? ')
v0 = float(v0) #making sure the input is a float

t = raw_input('How many seconds have gone? ')
t = float(t)   #making sure the input is a float

def test_y():  #test if the function is working
    computed = y(2, 1)
    expected = -2.905
    tol = 1e-10
    success = (computed - expected) < tol
    msg = 'something is wrong'
    assert success, msg
test_y()       #calling the test

q = y(v0,t)    #calling the function
print '''
The ball is now %.3f meters in the air''' %(q)        #printing the result

"""
Terminal> python ball_qa.py 

Only insert numbers

What is the start velocity (m/s)? 6.8
How many seconds have gone? 1.2

The ball is now 1.097 meters in the air
"""
