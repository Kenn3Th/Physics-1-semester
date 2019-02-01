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
This is the way i fetch the file:

Terminal> curl https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/funcif/lnsum.py >lnsum.py

Terminal> python lnsum.py > lnsum.dat

I saved the file as lnsum.dat, that is why I used this name in my code.

Terminal> python read_error.py 
"""
