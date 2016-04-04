""" 
This is our first exciting image
Written on class 04/02/2015
"""

import numpy as np
import matplotlib.pylab as plt
import math

ax = plt.subplot(111)
# Define variables 
lambda_wave = 5.     #wavelength in cm
k = 2. * np.pi / lambda_wave
xi = 1.              # in cm 
separation = 20. 
size = 1. * 100. # size of pic in cm
npixel = 500
dx = size / float(npixel)

# Define positions
x1c = size / 2. - separation / 2. 
y1c = size / 2. 
x2c = size / 2. + separation / 2. 
y2c = size / 2. 

xi_both = np.zeros(shape = (npixel,npixel)).astype('float')
# Compute image
for j in range(npixel):          #rows
	y = float(j) * dx   
	for i in range(npixel):  #column
		x = float(i) * dx
		r1 = np.sqrt( (x - x1c)**2 + (y - y1c)**2)
		r2 = np.sqrt( (x - x2c)**2 + (y - y2c)**2)
		xi1 = xi * np.sin(k * r1)
		xi2 = xi * np.sin(k * r2)
		xi_both[j,i] = xi1 + xi2

# plot
plt.imshow(xi_both,origin='lower',extent=([0,size,0,size]))
plt.gray()
ax.set_xlabel('x [cm]')
ax.set_ylabel('y [cm]')

plt.savefig('newplot.png',format='png')  #keep a hard copy of my figure
