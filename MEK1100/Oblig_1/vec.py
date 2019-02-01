from pylab import*; from seaborn import*
from velfield import hastighet

x,y,u,v = hastighet(7)
quiver(x,y,u,v)
xlabel('x-aksen')
ylabel('y-aksen')
savefig('4b.png')
show()
