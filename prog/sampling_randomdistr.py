"""
Produce a sample of points distributed homogeneously within
a sphere of given density profile: \rho = A r^alpha.
Method: Inverse transform 
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb
import math
from pylab import *
from scipy import *
import sys

#generate distribution within rmin, rmax and using nbin bins. 
rmin = 0.0   
rmax = 5.
nbin = 50

dr = (rmax - rmin) / float (nbin)
rbin = rmin + np.arange (nbin) * dr

alpha = -2.5    #slope of DENSITY profile, rho
rho = rbin ** alpha
beta = alpha + 3  # slope of mass profile (the cumulative distribution given a density PDF rho)
mass = rbin ** beta / rmax ** beta
mmax = np.max(mass)

fig1 = plt.figure (1)
ax1 = plt.subplot (111)
plt.plot (rbin, mass,'r-o')

nran = 10000

## --- here is the uniform sampling. Given a M(r), find the distribution of r that
##generates that M(r)
fig2 = plt.figure(2)

y = np.random.uniform (0, 1, nran)
rr = (y) ** (1 / beta) * rmax   #inverse of M(r)

nbins = 20
n, bins, patches = hist (rr, nbins)
plt.xlabel('r [kpc]',fontsize=15)
plt.ylabel('Number',fontsize=15)


## -----
# Compute the density obtained from the sampled points
rho_ = np.zeros (nbins)
for i in range (nbins):
	rho_[i] = n[i] / (bins[i + 1]**3 - bins[i]**3)  #number of points divided volume of shell

bins = bins[0 : nbins] + 0.5 * (bins[1] - bins[0])

xx = np.log (bins)
yy = np.log (rho_)

# plot density profile from generated sample
fig = plt.figure(3)
plt.plot(xx,yy,'ro',markersize=13)
plt.xlabel('log(r)',fontsize=15)
plt.ylabel(r'log($\rho$)',fontsize=15)

# fit obtained density profile and plot fit
coeff = np.polyfit(xx,yy,1) 
print 'coefficient from fit=', (coeff[0], alpha)

yy2 = xx*coeff[0] + coeff[1]
plt.plot(xx,yy2,'-b',linewidth=3)

pdb.set_trace()
