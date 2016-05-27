import numpy as np
import matplotlib.pyplot as plt
import pdb
from scipy import stats
import matplotlib.animation as animation

def brownian(n):
	x = np.random.randn(n)
	x = np.append(0.,x)
	x = np.cumsum(x)
	return x 

### plot 1 displacement ###
N=200
dis = brownian(N)
#plt.plot(np.arange(N+1),dis,'-',linewidth=5)
#pdb.set_trace()
## ------

fig1 = plt.figure(1)
#Generate a sample of particles diffusing. 
npart = 50
dis_all = np.zeros((N+1,npart))
x_all = np.zeros((N+1,npart))
y_all = np.zeros((N+1,npart))
for i in range(npart):
	x = brownian(N)
	y = brownian(N)
	dis_all[:,i] = np.sqrt(x**2 + y**2)
	x_all[:,i] = x
	y_all[:,i] = y
	plt.plot(np.arange(N+1),dis_all[:,i]**2,'-',linewidth=1,alpha=0.3)

# add average #
ave = np.sum(dis_all**2,axis=1) / float(npart)
plt.plot(np.arange(N+1),ave,'-k',linewidth=6)
plt.ylim(0,250)

### --- compute the diffussion coefficient ---
coeff = np.polyfit(np.arange(N+1),ave,1)
#slope,intercept,r_value,p_value,std_err = stats.linregress(np.arange(N+1),ave)

print 'slope 1=',coeff[0]/2.
#print 'slope 2=',slope/2.

# ---
fig2=plt.figure(2)
plt.hist(dis_all[-1,:])

## ---
## Create animation to show difussion 
fig3 = plt.figure(3)
fig3,ax = plt.subplots()

plt.xlim(-100,100)
plt.ylim(-100,100)
xx=([-1000,1000])
yy=([0,0])
plt.plot(xx,yy,':',linewidth=3,color='k')
plt.plot(yy,xx,':',linewidth=3,color='k')

line, = ax.plot(x_all[0,:],y_all[0,:],'ro')

def animate(i):
	line.set_ydata(y_all[i,:])
	line.set_xdata(x_all[i,:])
	return line,

ani = animation.FuncAnimation(fig3, animate, np.arange(1, 100),interval=100)

plt.show()


pdb.set_trace()
