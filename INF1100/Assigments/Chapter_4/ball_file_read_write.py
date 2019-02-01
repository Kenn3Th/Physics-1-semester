
def extract_data(filename): #function for sample file 'ball.dat'
    time = [] #time values
    with open(filename, 'r') as infile:
        lst = infile.readline().split()
        v0 = (eval(lst[-1])) #initial velocity
        infile.readline()
        tid = [] #making a nested list
        for line in infile:
            t = line.split()
            tid.append(t[0:])
        for t in range(len(tid)):
            for w in range(len(tid[t])): 
                ti = float(tid[t][w]) #breaking up the nested list to one list
                time.append(ti)
        time.sort()  #sorting the t values in an increasing order.
        return v0, time

def test_extract_data():
    v0, time = extract_data('ball.dat')
    t_expect = [0.042, 0.0519085, 0.10262264, 0.1117, 0.15592, 0.17383923,\
               0.2094294, 0.21342619, 0.21385894, 0.27, 0.28075, 0.29584013,\
                0.3464815, 0.35, 0.36807889, 0.372985, 0.39325246, 0.50620017,\
                 0.528, 0.53012, 0.57681501876, 0.57982969]
    t_computed = time
    v_expect = 3
    v_computed = v0
    tol = 1E-14
    success = (v_expect - v_computed) < tol and t_expect == t_computed
    msg = 'something went wrong'
    assert success, msg

test_extract_data() #calling test function

v0, time = extract_data('ball.dat') #calling function
    
with open('ball_file_write.dat', 'w') as outfile: #writing a new file
    outfile.write('-------------------------- \n')  
    outfile.write('  Time (s) | Y value (m)\n')
    outfile.write('--------------------------\n')
    for t in time: #implementing each time value in the formula 
        g = 9.81
        y = v0*t - 0.5*g*t**2 #calculating y(t)
        outfile.write(('%10.6f | %7.6f\n') %(t, y)) #writing the result in colums
"""
nothing appears in the terminal window.
program writes a new file based on sample file ball.dat:

'ball_file_write.dat'
-------------------------- 
  Time     | Y value
--------------------------
  0.042000 | 0.117348
  0.051909 | 0.142509
  0.102623 | 0.256211
  0.111700 | 0.273901
  0.155920 | 0.348514
  0.173839 | 0.373288
  0.209429 | 0.413152
  0.213426 | 0.416852
  0.213859 | 0.417243
  0.270000 | 0.452425
  0.280750 | 0.455635
  0.295840 | 0.458228
  0.346481 | 0.450602
  0.350000 | 0.449137
  0.368079 | 0.439697
  0.372985 | 0.436582
  0.393252 | 0.421211
  0.506200 | 0.261750
  0.528000 | 0.216564
  0.530120 | 0.211922
  0.576815 | 0.098475
  0.579830 | 0.090416
"""
