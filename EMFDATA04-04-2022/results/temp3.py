import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.fft import fft, fftfreq
from numpy.fft import fft, ifft
from scipy import signal

plt.style.use('seaborn-poster')

sr = 2000
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')

g= np.linspace(0,1,1000,endpoint=True)
y=signal.square(2*np.pi*1*g);
plt.plot(g,y)

plt.show()



X = fft(y) # FFT of a signal
N = len(X) # Length of X
#print (np.abs(X))
n= np.arange(N)
freq=np.fft.fftfreq(n=y.size, d=1/1000)
#print (freq)

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')


plt.subplot(122)
plt.plot(g, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()



