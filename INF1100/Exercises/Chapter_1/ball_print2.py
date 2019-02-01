v0 = 5
t = 0.6
g = 9.81
y = v0*t - 0.5*g*t**2
print """
At t=%f s, a ball with
initial velocity v0=%.3E m/s
is located at the hight %.2f m.
""" % (t, v0, y)

"""
Terminal>python ball_print2.py 

At t=0.600000 s, a ball with
initial velocity v0=5.000E+00 m/s
is located at the hight 1.23 m.
"""
