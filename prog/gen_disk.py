"""
PROGRAM TO GENERATE A DISK OF PARTICLES AND COMPUTE
EIGENVALUES AND EIGENVECTORS OF THE INERTIA TENSOR
#
WORKED IN CLASS APR. 14 2016
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb
import numpy.linalg as lin


# generate plane ----
npoint = 1000
x = 2. * np.random.rand(npoint) - 1.  #random number between -1 and 1
y = 2. * np.random.rand(npoint) - 1.  #random number between -1 and 1
z = 2. * np.random.rand(npoint) - 1.  #random number between -1 and 1
z *= 0.0001

# make it a disk ---
rad = np.sqrt(x**2 + y**2)
aux = rad < 1.
x1 = x[aux]
y1 = y[aux]
z1 = z[aux]

pos = np.zeros((len(x1),3))
pos[:,0] = x1
pos[:,1] = y1
pos[:,2] = z1

print  'len x and x1=',(len(x),len(x1))

plt.plot(x,y,'r.')
plt.plot(x1,y1,'b.')
plt.axis([-1.5,1.5,-1.5,1.5])

#----- compute inertia tensor
dist = np.sqrt(pos[:,0]**2 + pos[:,1]**2 + pos[:,2]**2)

A = np.zeros((3,3))
for i in range(3):
	for j in range(3):
		A[i,j] = np.sum(pos[:,i]*pos[:,j]/dist**2)

print 'done with inertia tensor'

## ---- get eigen vals and vect ---
x,v = lin.eigh(A)
print 'eigenvalues=',x
print 'eigenvect=',v


pdb.set_trace()
