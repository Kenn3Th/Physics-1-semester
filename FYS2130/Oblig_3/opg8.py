import numpy as np, matplotlib.pyplot as plt
from numpy.fft import fft
N = 500.0
x = 2*np.pi
t = np.linspace(0,10,N)
signal = np.sin(x*t)+np.cos(x*t)
FFT = fft(signal)/N
forste = FFT[0]
gjen = np.sum(signal)/N
diff = gjen - forste
print gjen, forste
"""
terminal >>
0.002 (0.002+0j)
"""
