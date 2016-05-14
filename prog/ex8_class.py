import numpy as np
import matplotlib.pyplot as plt
import pdb

#Define constants...

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
	r[:] = np.array([x,vx,y,vy])
	return r   #check this


tini = 0.
tend = 1000000.
N = 200000
h = 1000.

xpoint = np.zeros(N)
ypoint = np.zeros(N)
h_step = np.zeros(N)

r = np.array([4.e12,0.,0.,500.])

t = 0.
while t < tend:

	r1 = r.copy()

	while (redo == 1):
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

		rho = 30. * h * delta / (np.sqrt((r1[0]-r2[0])**2) + (r1[2]-r2[2])**2))

		if rho >= 1.:
			r[index??] = r1
			redo = 0
			t += 2h 
		else:
			redo = 1

		hnew = h * rho** 0.25
		
