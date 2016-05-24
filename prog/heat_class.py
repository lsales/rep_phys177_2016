import numpy as np
import matplotlib.pyplot as plt
import pdb

# constants
D = 4.25e-6
N = 101
L = 0.01   #in m
a = L/float(N)
h = 1.e-4

Thi = 50.
Tlo = 0.
Tmi = 20.
tini = 0. 
tend = 10.1

#times for outputs:
t1 = 0.01
t2 = 0.1
t3 = 0.4
t4 = 1.0
t5 = 10
acc = 1.e-5 

#IC
T = np.zeros(N)
T[0] = Thi
T[-1] = Tlo
T[1:N-1] = Tmi

Tp = np.zeros(N)
Tp = T.copy()

t = 0.
nstep = 0
c = h * D / a**2
while t < tend:
	for i in range(1,N-1):
		Tp[i] = T[i] + c * (T[i-1] + T[i+1] - 2.* T[i])

	#T, Tp = Tp, T
	T = Tp.copy()
	nstep += 1

	if np.abs(t - t1)<acc:
		plt.plot(T)
	if np.abs(t - t2)<acc:
		plt.plot(T)
	if np.abs(t - t3)<acc:
		plt.plot(T)
	if np.abs(t - t4)<acc:
		plt.plot(T)
	if np.abs(t - t5)<acc:
		plt.plot(T)

	t += h


pdb.set_trace()
