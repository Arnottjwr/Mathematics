# Plot to illustrate Tangent Bifurcation 
# Can vary values of r. Tangent point is r = 1 + sqrt(8)

import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 10})

# Logistic Map
def logistic(x,r):
    return r*x*(1 - x)

# Parameters 
r = 1 + np.sqrt(8)
x = np.linspace(0,1,500)
f3 = logistic(logistic(logistic(x,r),r),r)

# Plot   
fig,ax = plt.subplots(1,figsize = (10,6))
ax.set_ylim(0,1)
ax.set_title(f'$f^3(N_n)$ against $x$ for r = {r}')
ax.set_xlabel('$N_n')
ax.set_ylabel('$f^3(N_n)$')
ax.plot(x,f3)
ax.plot(x,x)
ax.grid()
plt.show()
