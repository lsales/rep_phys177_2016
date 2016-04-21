import numpy as np
from math import exp
import pdb


def f(x):
	return x - exp(1. - x**2)

x1 = 0.2
x2 = 0.5 

f1 = f(x1)
f2 = f(x2)
if f1 < 0. and f2 < 0.:
	print 'wrong initial values'
	pdb.set_trace() 
if f1 > 0. and f2 > 0.:
	print 'wrong initial values'
	pdb.set_trace() 
		
eps = 1.e-6

i = 0
while abs(x2-x1)>eps:
	i += 1
	x3 = (x2 + x1) / 2.
	f3 = f(x3)
	
	#if (f3 < 0. and f1<0.) or (f3 > 0. and f1>0.):
	if np.sign(f3) == np.sign(f1):
		x1 = x3
	if (f3 < 0. and f2<0.) or (f3 > 0. and f2>0.):
		x2 = x3

	
print 'i am out'
solution = (x2+x1) / 2.
print 'solution=',solution
print 'number of steps=',i


pdb.set_trace() 
