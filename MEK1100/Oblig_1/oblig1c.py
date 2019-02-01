from pylab import*
from seaborn import*

#variable jeg kan/maa velge selv. Enhet = []
g = 9.81               # [m/s^2]
v0 = 10.0              # [m/s]
t = linspace(0,2,50)   # [s]
#variable som er oppgitt/begrenset i oppgaven
theta = [pi/6, pi/4, pi/3]

for i in range(3):    
    x = (t*g)/(2*v0*sin(theta[i])) #[s][m/s^2]/[m/s] = (m/s)/(m/s) = 1
    y = x*tan(theta[i])*(1-x)
    plot(x,y)
    axis([0,1,0,0.5])
title(r'Plott av ukastvinklene $\theta = \frac{\pi}{6},\frac{\pi}{4},\frac{\pi}{3} $')
legend([r'$\theta = \frac{\pi}{6}$',r'$\theta = \frac{\pi}{4}$',\
        r'$\theta = \frac{\pi}{3}$'])
xlabel(r'$x^*=\frac{t*g}{2*v0*sin(\theta)}$')
ylabel(r'$y^*=x^*tan(\theta)(1-x^*)$')    
show()
savefig('1c.png')
