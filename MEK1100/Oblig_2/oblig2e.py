from oblig2 import*

#virvling
k = gradient(v,axis=1) - gradient(u,axis=0)
#konturplott
verdi = linspace(-1000,1000,9)
contourf(x,y,k,verdi)
colorbar()
#skilleflate
plot(xit,yit,'*',color='black')
#rektanglene
def rektangel(xi,yi,xj,yj):
    x1 = x[yi][xi]; x2 = x[yj][xj]
    y1 = y[yi][xi]; y2 = y[yj][xj]
    plot([x1,x2],[y1,y1], color='red')
    plot([x2,x1],[y2,y2], color='blue')
    plot([x1,x1],[y1,y2], color='black')
    plot([x2,x2],[y2,y1], color='green')
rektangel(34,159,69,169)
rektangel(34,84,69,99)
rektangel(34,49,69,59)
#Navngir akser +tittel
xlabel('X-akse')
ylabel('Y-akse')
title('Virvling')  
savefig('2e.png')
show()
