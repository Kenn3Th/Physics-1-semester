import numpy as np

x = np.linspace(0, 2, 22)
#y = x*(2-x)
y = np.cos(18*np.pi*x)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
