import numpy as np
import matplotlib.pyplot as plt

p = 17   # interest rate
N = 5    # number of years
n = 1    # year 1
x = 2500 # initial amount

outfile = open('growth_years_efficient.dat', 'w')
outfile.write('Growth years efficient \n')
outfile.write('-------------------------- \n')
outfile.write('Years:     |     amount: |\n')
outfile.write('-------------------------- \n')
outfile.write('1          |     2500.00 |\n')
while n < N:
    x = x + (p/100.0)*x
    n += 1
    outfile.write('%d          |     %.2f |\n' %(n, x))
outfile.write('--------------------------')
outfile.close()

"""
Terminal>python growth_years_efficient.py
"""
