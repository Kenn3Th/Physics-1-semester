from oblig2 import*
#Sirkulasjon
def sirkulasjon(xi,yi,xj,yj):
    dt = 0.5
    side1 = sum(u[yi,xi:xj+1]*dt)
    side2 = sum(v[yi:yj+1,xj]*dt)
    side3 = -sum(u[yj,xi:xj+1]*dt)
    side4 = -sum(v[yi:yj+1,xi]*dt)
    sirk = side1 + side2 + side3 + side4
    print 'Bunn:         %.5f' %(side1)
    print 'Hoyre side:   %.5f' %(side2)
    print 'Topp:         %.5f' %(side3)
    print 'Venstre side: %.5f' %(side4)
    return 'Sirkulasjon = %.5f' %(sirk)
#stokes sats
def stokes(x1,y1,x2,y2):
    dvx = gradient(v,0.5,axis=1)
    duy = gradient(u,0.5,axis=0)
    nXv = dvx - duy
    q = sum(nXv[y1:y2+1,x1:x2+1])*0.25
    return 'Stokes = %.5f'%(q)
#skriver ut informasjonen
print '----------------------------'
print 'Rektangel 1'
print sirkulasjon(34,159,69,169)
print stokes(34,159,69,169)
print 'Differanse = %.5f'%(2695.51409-2621.55870)
print '----------------------------'
print 'Rektangel 2'
print sirkulasjon(34,85,69,99)
print stokes(34,85,69,99)
print 'Differanse = %.5f'%(-60635.94012--61095.33233)
print '----------------------------'
print 'Rektangel 3'
print sirkulasjon(34,49,69,59)
print stokes(34,49,69,59)
print 'Differanse = %.5f'%(9.52102--12.21433)
print '----------------------------'
