import numpy as np

def loan(L, p, N):
    L = float(L)
    index_set = range(N+1)

    x = np.zeros(len(index_set))
    y = np.zeros(len(index_set))

    x[0] = L

    for n in index_set[1:]:
        y[n] = (p/(12.0*100))*x[n-1] + L/N
        x[n] = x[n-1] + p/(12.0*100)*x[n-1] - y[n]

    return x, y

print loan(1000,5,100)
