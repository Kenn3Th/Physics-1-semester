from numpy import linspace, sin
from matplotlib.pyplot import plot, show
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return sin(x)/x

n = 50
x_min = -10
x_max = 10

x = linspace(x_min, x_max, n+1)

plot(x, f(x))
show()
