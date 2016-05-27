import numpy as np
import matplotlib.pyplot as plt
import pdb


N = 200

def brownian(N):
	x = np.random.randn(N)
	x = np.append(0.,x)
	x = np.cumsum(x)
	return x


# Part 1 -- trayectory of single particle
#x = brownian(N)
#plt.plot(np.arange(N+1),x,'-',linewidth=3)

# Part 2 -- many particles
Npart = 100

dis_all = np.zeros((N+1,Npart))
for i in range(Npart):
	x = brownian(N)
	#plt.plot(np.arange(N+1),x**2,'-',linewidth=2,alpha=0.5)

	dis_all[:,i] = x

ave = np.sum(dis_all**2,axis=1) / float(Npart)
plt.plot(np.arange(N+1),ave,'-k',linewidth=6)
plt.ylim(0,250)

### --- Get D from <X^2>
time = np.arange(N+1)
coeff = np.polyfit(time,ave,1)

D = 0.5 * coeff[0]
print 'D=',D

## --- plot distribution at t=200 ---
fig2 = plt.figure(2)
plt.hist(dis_all[-1,:])

pdb.set_trace()

