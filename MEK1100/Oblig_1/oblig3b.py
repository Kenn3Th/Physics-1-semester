from pylab import*
from seaborn import*

#variable
n = linspace(-pi/2,pi/2,21)
Y,X = meshgrid(n,n,indexing='ij')
#funksjoner
vx = cos(X)*sin(Y)
vy = -sin(X)*cos(Y)
#plotting
streamplot(X,Y,vx,vy)
xlabel('x-aksen')
ylabel('y-aksen')
title('Plott av stromlinjene rundt origo langs x- og y-aksen')
savefig('3c.png')
show()
