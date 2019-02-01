import random, sys #imports random and sys

try:
    q = float(sys.argv[1])
    b = int(sys.argv[2])
except IndexError:
    print "Provide command-line arguments for stakes 'r' and N experiments"
    sys.exit(1)
except ValueError:
    print "Wait what?!? insert 2 numbers r and N!!"
    sys.exit(1)

r = float(sys.argv[1]); n = int(sys.argv[2]) #fetches numbers from cml

M = 0
for i in range(n):
    s = 0
    for j in range(4):
        die = random.randint(1,6)
        s += die
        #print 'die =',die 
    #print 'sum =', s
    if s < 9:
        M += r
        
print 'You have won',(M - n), 'Euro'

"""
Terminal> python sum_4dice.py 10 1000
You have won -460.0 Euro

Du kan fjerne # forann print i for loopen hvis du vil kontrolere om
terningene har 1-6 oyne og summene er korrekt
"""
