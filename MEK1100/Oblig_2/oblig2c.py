from oblig2 import*
from seaborn import*
#arrow-plot
n=11
quiver(
    x[::n, ::n],
    y[::n, ::n],
    u[::n, ::n],
    v[::n, ::n],
    units='width', width = 0.0015)
#Rectangles
def rektangel(xi,yi,xj,yj):
    x1 = x[yi][xi]; x2 = x[yj][xj]
    y1 = y[yi][xi]; y2 = y[yj][xj]
    plot([x1,x2],[y1,y1], color='red')
    plot([x2,x1],[y2,y2], color='blue')
    plot([x1,x1],[y1,y2], color='black')
    plot([x2,x2],[y2,y1], color='green')
rektangel(35,160,70,170)
rektangel(35,85,70,100)
rektangel(35,50,70,60)
#seperate flat
plot(xit,yit,'*',color='yellow')
#Giving name to the axes and sets a title.
xlabel('X-akse')
ylabel('Y-akse')
title('Vektor pil plott av hastigheten')
savefig('2c.png')
show() #Shows the plot
