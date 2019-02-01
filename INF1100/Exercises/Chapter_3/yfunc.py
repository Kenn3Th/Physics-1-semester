def yfunc(t, v0):
    g = 9.81
    return v0*t - 0.5*g*t**2

y = yfunc(1, 5)
print y
