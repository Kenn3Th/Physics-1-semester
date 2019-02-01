import random

N = [10, 10**2, 10**3, 10**6]
M = 0
for i in N:
    for j in range(i+1):
        r = random.random()
        if 0.5<=r<=0.6:
            M += 1
    print 'M = %g N = %i' %(M,i)
    print 'Probability  =', float(M)/i, 'when N = %i'%(i)

"""
Terminal> python compute_prob.py 
M = 1 N = 10
Probability  = 0.1 when N = 10
M = 12 N = 100
Probability  = 0.12 when N = 100
M = 112 N = 1000
Probability  = 0.112 when N = 1000
M = 100218 N = 1000000
Probability  = 0.100218 when N = 1000000
"""
