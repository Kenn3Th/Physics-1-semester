import numpy as np

N = [10, 10**2, 10**3, 10**6]

for i in N:
    r = np.random.random(i)
    r1 = r[r>0.5]
    r2 = r1[r1<0.6]
    prob = float(len(r2))/i
    print 'M = %d, N = %i' %(len(r2), i)
    print 'Probability =',prob
    
"""
Terminal> python compute_prob_vec.py 
M = 0, N = 10
Probability = 0.0
M = 11, N = 100
Probability = 0.11
M = 109, N = 1000
Probability = 0.109
M = 100110, N = 1000000
Probability = 0.10011
"""
