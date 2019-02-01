import random, sys #imports random and sys

try:
    t = sys.argv[1]; t = float(t)
except:
    print 'no command line arguments! Innsert number of eksperiments and n value', sys.exit()

try:
    q = sys.argv[2]; q = float(q)
except:
    print 'Innsert number of dices in command line!', sys.exit()
    
"""
exact = 11/36.0 for n = 2
"""
eksperiments, n = sys.argv[1], sys.argv[2] #fetches arguments from command line
eksperiments = int(eksperiments) #making string arguments to integers
n = int(n)

m = 0
for i in range(1,eksperiments+1):
    for j in range(1,n+1):
        die = random.randint(1,6)
        if die == 6:
            m += 1
print '---------------------------------------------------------------'
print 'if we have %i dice and does the eksperiment %i times' %(j,i)
print 'the probability is',(float(m)/j)/i,'percent to get 6 eyes on a die'
print '---------------------------------------------------------------'
print 'FUN FACT'
print 'The exact probability to get 6 eyes on a die is',11./36
print 'percent for n = 2, the approximate probability is',(float(m)/j)/i,'for n = %i' %(n)
print 'relation between exact and approximate =', ((float(m)/j)/i)/(11./36)
print '---------------------------------------------------------------'

"""
Terminal> python one6_ndice.py 10000 2
---------------------------------------------------------------
if we have 2 dice and does the eksperiment 10000 times
the probability is 0.16335 percent to get 6 eyes on a die
---------------------------------------------------------------
FUN FACT
The exact probability to get 6 eyes on a die is 0.305555555556
percent for n = 2, the approximate probability is 0.16335 for n = 2
relation between exact and approximate = 0.5346
---------------------------------------------------------------
"""
