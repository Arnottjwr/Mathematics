## Fourier representation of a plucked string, obtained from solving the wave equation 

import numpy as np
import matplotlib.pyplot as plt
from WaveFunctions import plucked_string

L = 65 
c = 1
a = 1
p = 10 # Plucking Posn
x = np.linspace(0,65,500)  
t = 0

fig, ax = plt.subplots(1, figsize=(15, 10))

list = []
for i in range(1,21):  # Loop through modes
    u = plucked_string(x, t, L, p, c, a, i)
    if i == 1:
        a1 = u[31]
        a2 = u[115]
    list.append(u)
    ax.plot(x, u ,label = f'n = {i}') # Plot wave modes 
r = np.array(list, dtype = object)
ori = np.sum(r,axis = 0)

ax.plot(x,ori, label = "Superposition Wave", linewidth = 2.5, color = 'k') # Plot superposition 
ax.plot(([4,4]),([0,a1]),'k') #Bridge Pickup Line
ax.plot(([15,15]),([0,a2]),'k') #Neck Pickup Line
ax.set_xlabel('x')
ax.set_ylabel('Amplitude') 
ax.set_title(f'Plucked at {p}cm')   
ax.scatter(4,0,marker="o",color='r',s=130, zorder=2,label = 'Bridge Pickup') # Bridge Pick-up
ax.scatter(15,0,marker="o",color='b',s=130, zorder=2,label = 'Neck Pickup') # Neck pick-up
ax.scatter(p,0,marker="x",color='k',s=130, zorder=2,label = 'Plucking Point') # Bridge Pick-up
ax.text(-2.5,-0.1,'Bridge',fontsize=13)
ax.text(65,-0.05,'Headstock',fontsize=13)    
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.grid()
