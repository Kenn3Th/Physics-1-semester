v0 = 5
g = 9.81
yc = 0.2
import math as m
t1 = (v0 - m.sqrt(v0**2 - 2*g*yc))/g
t2 = (v0 + m.sqrt(v0**2 - 2*g*yc))/g
print 'At t=%g s and %g s, the hight is %g m' % (t1, t2, yc)

"""
Terminal>python ball_print3.py 
At t=0.0417064 s and 0.977662 s, the hight is 0.2 m
"""
