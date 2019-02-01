import random, sys
import numpy as np

try:
    g = int(sys.argv[1])
except IndexError:
    print "Provide command-line arguments for N"
    sys.exit()
except ValueError:
    print "What are you doing? N = number of eksperiments!!"
    sys.exit()
    
def roll_dice(n):#en funksjon som bestemmer en tilfeldig sum av aa kaste to terninger
    s = []
    for i in xrange(n):
        r = random.randint(1,6)
        g = random.randint(1,6)
        s.append(r + g)
    return s

n = int(sys.argv[1]) #henter hvo rmange ganger man kaster terningene (n) fra cml
lst = np.sort(roll_dice(n)) #sorterer de tilfeldige summene i lista

#laget en dictinoary med de forskjellige summene som er mulig aa faa
result = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,\
          "8": 0, "9": 0, "10": 0, "11": 0, "12": 0} 

for i in lst: #legger nummerene i lista over i dictionary
    result['%i'%i] += 1
    
#lager en ny dictionary med sannsynligheten for aa faa de forskjellige summene
prob = {} 
for j in range(2,13):
    p = result["%i" %j]/float(n)
    prob["%d"%j] = p
    
#Dette er en dictionary med de eksakte sannsynlighetene
exact_prob = {'2': 0.03, '3': 0.06, '4': 0.08, '5': 0.11, '6': 0.14,\
              '7': 0.17, '8': 0.14, '9': 0.11, '10': 0.08, '11': 0.06, '12': 0.03}

#gjor om dictionarys om til lister slik at jeg kan skrive de ut i et pent format.
numbers = []
aprox = []
exact = []
for f in range(2,13):
    ap = prob["%d"%f]
    ex = exact_prob["%d"%f]
    aprox.append(ap)
    exact.append(ex)
    numbers.append(f)
    
print '--------------------------------------------'
print 'Eye dice |   Probability for getting that  |'
print '--------------------------------------------'
for a, e, n in zip(aprox, exact, numbers):
    print 'Sum = %2.i | Exact = %g, Approximate = %.2f' %(n,e,a)
print '--------------------------------------------'

"""
Terminal> python freq_2dice.py 1000
--------------------------------------------
Eye dice |   Probability for getting that  |
--------------------------------------------
Sum =  2 | Exact = 0.03, Approximate = 0.03
Sum =  3 | Exact = 0.06, Approximate = 0.07
Sum =  4 | Exact = 0.08, Approximate = 0.08
Sum =  5 | Exact = 0.11, Approximate = 0.09
Sum =  6 | Exact = 0.14, Approximate = 0.15
Sum =  7 | Exact = 0.17, Approximate = 0.16
Sum =  8 | Exact = 0.14, Approximate = 0.14
Sum =  9 | Exact = 0.11, Approximate = 0.12
Sum = 10 | Exact = 0.08, Approximate = 0.09
Sum = 11 | Exact = 0.06, Approximate = 0.05
Sum = 12 | Exact = 0.03, Approximate = 0.03
--------------------------------------------
"""
