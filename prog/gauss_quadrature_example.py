"""
Simple program to use the Gaussian Quadrature method to solve de integral
of f(x)=x^4 - 2x + 1 between [0,2]. We use a function provided with the book
(gaussxw.py) to compute the evaluating-points and weights. We also compare
our result with the intrinsic function by scipy: fixed_quad.
"""

from gaussxw import gaussxw
import numpy as np
from scipy.integrate import quad,fixed_quad
import pdb

## --- define function to integrate ---
def f(x):
	return x**6 - 2.*x + 1.


## define constants
a = 0.   #lower limit of integration
b = 2.   #upper limit of integration
N = 6    #number of "slices"

# get weights and positions
x1,w1 = gaussxw(N)
x1_new = 0.5 * (b - a) * x1 + 0.5 * (b + a)
w1_new = 0.5 * (b - a) * w1

# compute integral
s = 0
for k in range(N):
	s += w1_new[k] * f(x1_new[k])

print 's=',s


## new way ##  
# using scipy pre-defined function with given N
I = fixed_quad(f,a,b,n=N)
print 'integral fixed degree gauss', I[0]

pdb.set_trace()
