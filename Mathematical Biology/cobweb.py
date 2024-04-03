"""
Plot to illustrate intermittency in the logistic map 
Code partly adapted from Christian: https://scipython.com/blog/cobweb-plots/
"""
import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 10})

# Logistic Map
def logistic(x,r):
    return r*x*(1 - x)

#f^3 logistic map
def f3(x,r):
    return logistic(logistic(logistic(x,r),r),r)

# Parameters 
r = 3.823
x = np.linspace(0,1,500)

# Plot
fig,ax = plt.subplots(1,figsize = (10,6))
nmax = 50           # Max cobweb iterations 
x0 = 0.5            # Initial Point 
ax.plot(x,f3(x,r))  # Period-3 Map
ax.plot(x,x)        # y = N 

# Cobweb 
px, py = np.empty((2,nmax+1,2))
px[0], py[0] = x0, 0
for n in range(1, nmax, 2):
    px[n] = px[n-1]
    py[n] = f3(px[n-1], r)
    px[n+1] = py[n]
    py[n+1] = py[n]
ax.plot(px, py, c='b', alpha=0.7)

# Plot   
ax.set_title(f'$f^3(N_n)$ against $x$ for r = {r}')
ax.set_xlabel('$N_n')
ax.set_ylabel('$f^3(N_n)$')

# Toggle to zoom in to see intermittency 
# ax.set_ylim(0.4,0.6)
# ax.set_xlim(0.4,0.6)
ax.grid()
plt.show()