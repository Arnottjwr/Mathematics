'''
Code to test iterations of the logistic difference equation for differing values of control parameter r 
The logistic map displays rich dynamical behaviour. As the control parameter r (0 < r < 4) varies, 
we observe period doubling bifurcations. See the Bifurcation diagram plot for code to plot a Bifurcation diagram 
'''

import numpy as np 
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})

### Logistic Map 
def logistic(x, r):
    return r*x*(1-x)

### Inital Data 
r = 0.5 # Control Parameter 
initial = 0.5 # Inital Value 
n = 75 # Iterations 

### Arrays 
x = np.linspace(0,n,n)
y = np.zeros_like(x)
y[0] = initial

### Iterate 
for i in range(1,n):
    y[i] = logistic(y[i-1],r)

### Plot   
fig,ax = plt.subplots(1,figsize = (10,6))
ax.set_ylim(0,1)
ax.set_title(f'{n} iterations of $f(N) = rN(1-N) $ with r = {r} and inital point = {initial}')
ax.set_xlabel('n')
ax.set_ylabel('N')
ax.plot(x,y,'b')
ax.grid()
plt.show()
