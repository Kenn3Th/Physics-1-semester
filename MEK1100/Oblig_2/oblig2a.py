from oblig2 import*
#Putting the matrices and vectrs in a list
dat = [x,y,u,v,xit,yit]
#Checking the size of the matrices and vectors
for j in range(6):
    value = []
    indx = ['x','y','u','v','xit','yit']
    for i in dat:
        value += [shape(i)]
    if j < 4:
        print 'Matrisen %s har (x,y)' %(indx[j])
        print value[j]
    elif j >= 4:
        print 'Vektoren %s har (x,y)' %(indx[j])
        print value[j]
#test functions. 
#Checking if x is regulated with an interval on 0.5.
def test_x(q):
    for i in q:
        for j in range(194-1):
            tst = i[j+1]-i[j]
            sucsess = 0
            if tst == 0.5:
                sucsess
            else :
                print 'something went wrong'
#Checking if y is regulated with an interval on 0.5.
#and if it takes the whole diameter of the pipe.
def test_y(q):
    ykor = [] 
    for i in y:
        ykor += [i[1]]
        if abs(i[1]) > 50:
            print 'Overstiger diameteren!'
        else:
            ykor
    for j in range(194):
        tst = ykor[j+1]-ykor[j]
        success = 0
        if tst == 0.5:
            success
        else :
            print 'this is not right'
#Calling the test functions
test_x(x)
test_y(y)
