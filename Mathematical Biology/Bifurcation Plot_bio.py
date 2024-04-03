"""
Plots a Bifurcation Diagram of the Logistic map
Credit: https://ipython-books.github.io 
"""
# Import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt 

# Logistic Map 
def logistic(x,r):
    return r*x*(1-x)

# Define iterations 
n = 100000
iterations = 1000
last = 100

# Define Range of parameters
r = np.linspace(0, 25, n)
x = 1e-5 * np.ones(n)

# Iterate 
fig, ax1 = plt.subplots( 1, figsize=(8, 5),sharex=True)
for i in range(iterations):
    x = logistic(x, r)
    if i >= (iterations - last):
        ax1.plot(r, x, ',b', alpha=.25)
# Plot
ax1.set_xlim(0,4)
ax1.set_ylim(0,1)
ax1.set_title("Bifurcation diagram of $f(N) = rN(1 - N)$")
ax1.set_xlabel('r')
ax1.set_ylabel('N')
plt.show()
