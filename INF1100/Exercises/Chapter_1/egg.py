from math import pi, log

M = 67
c = 3.7
K = 5.4e-3
rho = 1.038

Tw = 100
To = 4
Ty = 70


time = (M**(2.0/3.0)*c*rho**(1.0/3.0))/(K*pi**2*(4*pi/3)**(2.0/3.0))\
  *log(0.76*(To-Tw)/(Ty-Tw))

minutes = int(time/60)
sec = int(time%60)
print '''It wil take %g seconds or %g minutes and %g seconds
to get the egg to be 70 degrees inside straight from the refrigdirator''' % (time, minutes, sec)

"""
Terminal>In [9]: run egg.py
It wil take 396.576 seconds or 6 minutes and 36 seconds
to get the egg to be 70 degrees inside straight from the refrigdirator
"""
