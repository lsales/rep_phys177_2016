"""
Modified version of laplace.py to perform Gauss-Steidel method + overrelaxation. 
End of class 15.
"""
from numpy import empty,zeros,max,ones,array
from pylab import imshow,gray,show
import pdb
import numpy as np

# Constants
M = 100         # Grid squares on a side
V = 1.0         # Voltage at top wall
target = 1e-6   # Target accuracy
w = 0.9 #2.9  #0.9       #overrelaxation parameter

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phi[0,:] = V

def phi0(i):
	phi1 = 0.
	if i == 0:
	   phi1 = V
	return phi1


# Main loop
delta = 1.0
nstep = 1
aux_index = np.arange(101).astype('int')
while delta>target:

    delta = target

    print 'second loop',nstep
    for i in range(M+1):
        for j in range(M+1):
    		#print 'i,j=',(i,j)
       		if i==0 or i==M or j==0 or j==M:
                	phi[i,j] = phi0(i) 
       	       	else:
			phi_old =  phi[i,j].copy()
               		phi[i,j] = (1.+w)*(phi[i+1,j] + phi[i-1,j] \
                                + phi[i,j+1] + phi[i,j-1])/4. - w * phi[i,j]

    			delta = max([delta,abs(phi_old - phi[i,j])] )   #keep max. difference to check convergence
		
		
    # count number of steps
    nstep += 1
    print 'nstep=', (nstep,delta)

# Make a plot
imshow(phi)
gray()

pdb.set_trace()
show()
