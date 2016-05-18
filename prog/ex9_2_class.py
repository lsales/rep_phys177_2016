import matplotlib.pyplot as plt
import numpy as np
import pdb

V = 1.
N = 101
L = 1.
a = 1. * 0.01  #each bin = 1cm
acc = 1.e-6
eps0 = 8.854187817   #C^2/(N*m)


def rho(x,y):
	x *= 100.  #in cm   
	y *= 100.
	rho1 = 0.
	if (x > 60.) & (x<80.) & (y >20.) & (y<40.):
		rho1 = + 1.
	if (x > 20.) & (x<40.) & (y > 60.) & (y<80.):
		rho1 = -1.
	return rho1



dx = L / float(N)
dy = L / float(N)
a = dx

phi = np.zeros((N,N))
phiprime = np.empty((N,N))

delta = 1.
while delta > acc:
	for i in range(N):
		x = float(i) * dx
		for j in range(N):
			y = float(j) * dy

			rho_ij = rho(x,y)

			if (i==0) | (j==0) | (i == N-1) | (j== N-1):
				phiprime[i,j] = 0. #phi[i,j]
			else:
			 	phiprime[i,j] = 1./4. * (phi[i-1,j]+phi[i+1,j]+phi[i,j-1]+phi[i,j+1]) \
						+ 1./4. * a**2 * rho_ij / eps0



	delta = np.max(np.abs(phi - phiprime)) 
	print delta
	phi = phiprime.copy()


plt.imshow(phi.T)
plt.gray()
pdb.set_trace()
