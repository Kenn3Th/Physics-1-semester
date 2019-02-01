A = 1000.0
p = 5.0
n = 3.0
q = A*(1 + p/100)**n

print '''After 3 years %.f Euro has grown to
%.2f Euro with %.g precent interest''' %(A, q, p)

"""
Terminal>python interest_rate.py 
After 3 years 1000 Euro has grown to
1157.63 Euro with 5 precent interest
"""
