"""
This program uses the trapezoidal rule to integrate the
function: x^4 - 2x + 1, in the range [0,2] and using N=10 slices
"""
import numpy as np
import math

## make a pre-defined function with f(x)
def f(x):
	return x**4 - 2.*x + 1.

## --- start trapezoid calculation
a = 0. #comment
b = 2.
N = 10

h = (b - a) / float(N)
I = f(a) + f(b)
for k in range(1,N):
	I = I + 2. * f(a + k*h)

I = I * 0.5 * h
print  'result I=',I
