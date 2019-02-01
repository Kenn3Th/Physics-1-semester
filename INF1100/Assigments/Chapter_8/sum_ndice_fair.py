import random, sys #imports random and sys

try:
    q = float(sys.argv[1])
    b = int(sys.argv[2])
except IndexError:
    print "Provide command-line arguments for stakes 'r' and N experiments"
    sys.exit(1)
except ValueError:
    print "Wait what?!? insert 2 whole numbers r and N!!"
    sys.exit(1)

r = float(sys.argv[1]); n = int(sys.argv[2]) #fetches numbers from cml

M = 0
prob = 0
for i in range(n):
    s = 0
    for j in range(4):
        die = random.randint(1,6)
        s += die
        #print 'die =',die
    #print 'sum =', s
    if s < 9:
        M += r
        prob += 1

print 'You have won',(M - n), 'Euro'
print 'The probability of winning is', float(M)/n

"""
The probability is ca 5% so r needs to be 1/0.05 = 20 for it to be a fair game.

Terminal> python sum_ndice_fair.py 20 100
You have won 0.0 Euro
The probability of winning is 1.0
"""
