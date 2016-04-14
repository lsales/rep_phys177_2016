"""
Example in class Apr. 14 to compute derivatives with
the central difference formula and compare with intrinsice
numpy function "gradient"
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 2.*x**3 + 5.

x = np.arange(10).astype('float')
f = f(x)
#f = np.array([1, 2, 4, 7, 11, 16], dtype=np.float)

h = 1.
N = len(f)
deriv = np.zeros(N)
for i in range(N):
	if i == 0:	
		deriv[i] = (f[1] - f[0]) / h
		continue
	if i == N-1:
		deriv[i] = (f[i] - f[i-1]) / h
		continue
	
	deriv[i] =  (f[i+1] - f[i-1]) / (2. * h)

print 'derivative=', deriv

### using intrinsic function ###
deriv_np = np.gradient(f)

print 'derivative numpy=',deriv_np

