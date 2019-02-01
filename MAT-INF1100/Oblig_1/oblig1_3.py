n = eval(raw_input('n? '))
i = eval(raw_input('i? '))

s = 1
    
for j in range(1,(n+1-i)):
    s = s * float(i+j)/float(j)

print '%.14e' %s

"""
Terminal> python oblig1_3.py 
n? 9998
i? 4
416083629102505
 
n? 100000
i? 70
8.14900007813826e+249

n? 1000
i? 500
2.70288240945437e+299

"""
