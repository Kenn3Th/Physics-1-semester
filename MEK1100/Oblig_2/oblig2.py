import scipy.io as sio
from pylab import*

data = sio.loadmat("data.mat")
x = data.get("x")
y = data.get("y")
u = data.get("u")
v = data.get("v")
xit = data.get("xit")
yit = data.get("yit")
