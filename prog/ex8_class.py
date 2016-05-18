import numpy as np
import matplotlib.pyplot as plt
import pdb

#Define constants...
G = 6.6738e-11 # m**3 kg**-1 s**-2         Gravitational Constant
M = 1.9891e30 # kg      Mass of the Sun
delta = 3.16887e-5 #m per year # convert to seconds   given 1km/year need to convert to m/sec   1 year = 31556926 seconds



def f(r):
	x = r[0]
	vx = r[1]
	y = r[2]
	vy = r[3]
	rdis = np.sqrt(x**2 + y**2)
	x = vx
	vx = - G * M * r[0] / rdis**3 
	y = vy
	vy = - G * M * r[2] / rdis**3
	return np.array([x,vx,y,vy],float)


tini = 0.
#tend = 1000000.
tend = 3.1e9 #final time
N = 20000
h = 2000000

xpoint = np.zeros(N)
ypoint = np.zeros(N)
tpoint = np.zeros(N)
h_step = np.zeros(N)

r = np.array([4.e12,0.,0.,500.])

t = 0.
nstep = 0L
while t < tend:

	redo = 1
	while (redo == 1):
		r1 = r.copy()
		for i in range(2):
			# use 4th-RK
			k1 = h * f(r1)
			k2 = h * f(r1 + 0.5 * k1)
			k3 = h * f(r1 + 0.5 * k2)
			k4 = h * f(r1 + k3)
			r1 += 1./6. * (k1 + 2.*k2 + 2.*k3 + k4) 
	
		r2 = r.copy()
		# use 4th-RK
		k1 = 2.*h * f(r2)
		k2 = 2.*h * f(r2 + 0.5 * k1)
		k3 = 2.*h * f(r2 + 0.5 * k2)
		k4 = 2.*h * f(r2 + k3)
		r2 += 1./6. * (k1 + 2.*k2 + 2.*k3 + k4) 

		var = np.sqrt((r1[0]-r2[0])**2 + (r1[2]-r2[2])**2)
		if var > 0: 
			rho = 30. * h * delta / var
		else:
			rho = 10.

		if rho >= 1.:
			r = r1
			redo = 0
			t += 2.*h 
		else:
			redo = 1

		hold = h
		h = hold * rho** 0.25
		if h > 2.*hold: h = 2.*hold

	xpoint[nstep] = r1[0]
	ypoint[nstep] = r1[2]
	tpoint[nstep] = t
	h_step[nstep] = hold

	nstep += 1
	print 'nstep=, h=', (h,nstep)

# re-shape arrays with needed number of elements
tpoint = tpoint[0:nstep]
xpoint = xpoint[0:nstep]
ypoint = ypoint[0:nstep]
h_step = h_step[0:nstep]


#plt.figure(1)
#plt.plot(xpoint, ypoint)
#pdb.set_trace()

### 
# plot orbit as a function of time
dist = np.sqrt(xpoint**2 + ypoint**2)
plt.subplot(2,1,1)
plt.plot(tpoint,dist,'--',linewidth=2)
plt.title("Orbit as a Function of Time - Two Orbits")
plt.xlabel('Time [sec]')
plt.ylabel('Distance [m]')

# plot step size
plt.subplot(2,1,2)
ax1 = plt.subplot(2,1,2)
plt.plot(tpoint,h_step,'-',linewidth=2)
ax1.set_yscale('log')
plt.title("Step size vs Time - Two Orbits")
plt.xlabel("Time [sec]")
plt.ylabel("Log of Step Size")


pdb.set_trace()
		
