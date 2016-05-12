"""
Lorenz attractor -- Exercise 8.3 from the book
"""
import numpy as np
import matplotlib.pyplot as plt
import pdb
from mpl_toolkits.mplot3d import Axes3D

def f(r, t, s_cte = 10., r_cte=28., b_cte=2.667):
	x = r[0]
	y = r[1]
	z = r[2]
	fx = s_cte * (y - x)
	fy = r_cte*x - y - x * z
	fz = x*y - b_cte*z
	return np.array([fx,fy,fz],float)


a = 0.
b = 50.
N = 1000 #10000 #15000   #p 15
h = (b - a) / float(N)
ic = np.array([1.,1.,1.])
#ic = np.array([0.,1.,0.])
#ic = np.array([1.,1.,15.])
tpoints = np.linspace(a,b,N)

xpoints = np.zeros(N)
ypoints = np.zeros(N)
zpoints = np.zeros(N)
r = ic

for it in range(N): 
    t = tpoints[it]
    xpoints[it] = r[0]
    ypoints[it] = r[1] 
    zpoints[it] = r[2]
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

#plt.plot(tpoints,ypoints,'r-')
fig = plt.figure(1)
ax = fig.gca(projection='3d')
ax.plot(xpoints,ypoints,zpoints)

pdb.set_trace()

