from pylab import*;
import streamfun as st
# i) n = 5
x,y,psi = st.streamfun(5)
contour(x,y,psi)
xlabel('x-akse')
ylabel('y-akse')
title('Streamfun')
savefig('4a5.png')
show()
# ii) n = 30
x,y,psi = st.streamfun(30)
contour(x,y,psi)
xlabel('x-akse')
ylabel('y-akse')
title('Streamfun')
savefig('4a30.png')
show()
