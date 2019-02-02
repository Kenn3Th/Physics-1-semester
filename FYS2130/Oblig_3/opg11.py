import numpy as np, matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import urllib2
#Behandle data
data = urllib2.urlopen("http://www.sidc.be/silso/DATA/SN_y_tot_V2.0.txt")
times = []
sunspots = []
for line in data:
    cols = line.split()
    times.append( float(cols[0]) )
    sunspots.append( float(cols[1]) )
#Array    
tid = np.array(times)
solflekker = np.array(sunspots)
N = float(len(solflekker))
#Fast fourier transformasjon
fourier = fft(solflekker)/N
fs = 1.0/(tid[1]-tid[0])
freq = np.linspace(0,fs,N)
#Plot
plt.subplot(1,2,1)
plt.plot(tid, solflekker,'-b') #Tidsbilde
plt.xlabel('Time, years')
plt.ylabel('Sunspots')
plt.title('Time domain')
plt.subplot(1,2,2)
plt.plot(freq,np.abs(fourier)) #frekvensbilde
plt.xlabel('Frekvens, $years^{-1}$')
plt.ylabel('Fourierkoeff $|X(f)|$')
plt.title('Frequency domain')
plt.axis([-0.01,0.5,0,80])
plt.show()

