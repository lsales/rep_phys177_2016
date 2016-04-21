import numpy as np
from math import exp,log,sqrt
import pdb

def f(x):
	#return 2. - exp(-x)
	#return exp(1.-x**2)	
	return sqrt(1.-log(x))	


x = 0.5
for i in range(100):
	x = f(x)
	print x

pdb.set_trace()
