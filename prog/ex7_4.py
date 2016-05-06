"""
Exercise 7.4 in book (pg. 317)
plus extra examples for "low-pass filter", "high-pass filter" and "band filters".
"""

import numpy as np
from numpy.fft import rfft,irfft
import matplotlib.pyplot as plt
import pdb

# --- copy previous function to compute DFT coefficients and compare with FFT
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c





# -- load data ----
filein = 'dow.txt'
y = np.loadtxt(filein)
# ---

N = len(y)
y -= (np.sum(y)/float(N))
plt.figure(1)
ax = plt.subplot(111)
plt.plot(np.arange(N),y,'r-',linewidth=3)
plt.xlabel('Days')
plt.ylabel('Stock market price')

coeff = rfft(y)
nc = len(coeff)

ax.text(600,3500,'Signal',color='red',fontsize=12)
### --- plot full power spectrum ---

plt.figure(2)
ax1 = plt.subplot(111)
plt.plot(np.arange(nc),np.abs(coeff)**2,linewidth=3)
ax1.set_yscale('log')
plt.axis([0,500,1.e7,1e12])
plt.xlabel('frequency')
plt.ylabel('$|c_k|^2$')

### ------
## speed test ### 
#print 'starting direct'
#ck_ = dft(y)

print 'done with direct'
ck_fft =  rfft(y)
print 'done with FFT'

####
## low pass filter ---

# compute 10%
nc_low = int(nc * 0.1)
coeff_new = coeff.copy()
coeff_new[nc_low:-1] = 0.


ynew = irfft(coeff_new)
plt.figure(1)
plt.plot(np.arange(N),ynew,'g--',linewidth=3)

ax.text(600,3000,'Low pass filter',color='green',fontsize=12)
## high-pass filter ---

# compute 10%
nc_high = int(nc * 0.9)
coeff_new2 = coeff.copy()
coeff_new2[0:nc_high-1] = 0.


ynew2 = irfft(coeff_new2)
plt.figure(1)
plt.plot(np.arange(N),ynew2,'b-',linewidth=3)
ax.text(600,2500,'High pass filter',color='blue',fontsize=12)

pdb.set_trace()
## band-pass filter ---

# compute 10%
nc_high = int(nc * 0.9)
coeff_new2 = coeff.copy()
coeff_new2[0:nc_low-1] = 0.
coeff_new2[nc_high:-1] = 0.


ynew2 = irfft(coeff_new2)
plt.figure(1)
plt.plot(np.arange(N),ynew2,'-',color='magenta',linewidth=1)
ax.text(600,2000,'Band-pass filter',color='magenta',fontsize=12)




pdb.set_trace()
