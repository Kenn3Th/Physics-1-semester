infile = open('lnsum.dat', 'r')

for i in range(24):
    infile.readline()
    
epsi = []
ex_er = []
k = []
          
for line in infile:
    words = line.split()
    epsi.append(float(words[1].strip(',')))
    ex_er.append(float(words[4].strip(',')))
    k.append(float(words[5].strip('n=')))

infile.close()

import numpy as np
import matplotlib.pyplot as plt

epsilon = np.array(epsi)
exact_error = np.array(ex_er)
n = np.array(k)

plt.semilogy(n,epsilon)
plt.semilogy(n,exact_error)
plt.legend(['epsilon','exact error'])
plt.title('Epsilon vs exact error')
plt.xlabel('n')
plt.ylabel('ln')
plt.show()

"""
Jeg hentet inn filen paa denne maaten:

Terminal> curl https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/funcif/lnsum.py >lnsum.py

Terminal> python lnsum.py > lnsum.dat

Jeg lagret filen som lnsum.dat, jeg brukte derfor dette navnet i koden min.

Terminal> python read_error.py 
"""
