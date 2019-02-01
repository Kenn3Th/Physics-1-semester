from math import sqrt, exp, pi

m = 0
s = 2.0
x = 1.0
f = ((1.0)/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2) #Formula

print f

"""
Terminal>python gaussian_function.py 
0.176032663382
"""
