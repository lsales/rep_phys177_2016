import matplotlib.pyplot as plt
import numpy as np
import pdb

V = 1.
N = 101
a = 1. * 0.01   #each bin = 1cm
acc = 1.e-3


phi = np.zeros((N,N))
phiprime = np.empty((N,N))

phi[:,0] = V
delta = 1.
while delta > acc:
	for i in range(N):
		for j in range(N):

			if (i==0) | (j==0) | (i == N-1) | (j== N-1):
				phiprime[i,j] = phi[i,j]
			else:
			 	phiprime[i,j] = 1./4. * (phi[i-1,j]+phi[i+1,j]+phi[i,j-1]+phi[i,j+1])



	delta = np.max(np.abs(phi - phiprime)) 
	phi = phiprime.copy()


plt.imshow(phi.T)
plt.gray()
pdb.set_trace()
