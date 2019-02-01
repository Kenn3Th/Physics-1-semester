def v(r, n):
    R = 1; Bet = 0.02; gam = 0.02;
    return ((Bet/2*gam)**(1./n))*(float(n)/(n + 1))*(R**((1+1.0)/n) - r**((1+1.0)/n))

r = float(raw_input('insert r '))
n = float(raw_input('insert n '))
print v(r, n)
