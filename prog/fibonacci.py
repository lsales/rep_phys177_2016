"""
This program is inspired in the discussion we had in class, 04/02/2015.
It generates the numbers smaller than 1000 in the Fibonacci Series 
(it actually stops after the first time the series go above 1000).
We added extra small features:
- step counter
- keep values in a list or array
- plot
"""
import numpy as np
import math
import matplotlib.pyplot as plt

# -- initialize "axes" object for later --
ax = plt.subplot(111)
# ----


f1 = 0
f2 = 1
next = f1 + f2

n = 0    #will introduce a steps counter
keep_val = []    #initialize a list to store values from the series

while(next < 1000):
	f1 = f2
	f2 = next
	next = f1 + f2 
	print next

	n += 1   #add step
	keep_val.append(next)

print 'done'
print 'number of steps= ',n

#you can convert the list to a numpy-array if wanted (not needed for this excercise)
keep_val_array = np.array(keep_val).astype('int32')

## we can plot the evolution of the series as the function of steps:

x = np.arange(n)   #creates a n-dim array from 0 to n-1
x[:] += 1     #now x goes from 1 to n
 
plt.plot(x,keep_val,'o-',color='red',linewidth=3,markersize=7)  # "o" refers to the symbol type (in this case circle) and "-" for solid line
ax.set_xlabel('step number')
ax.set_ylabel('Fibonacci number')
