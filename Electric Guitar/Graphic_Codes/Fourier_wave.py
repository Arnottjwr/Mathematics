from WaveFunctions import plucked_string

L = 65 
c = 10
a = 1
p = [5,10,15] # Plucking Posn
x = np.linspace(0,65,500)  
t = 0

fig, ax = plt.subplots(3,1, figsize=(15, 25))

for j in range(3):
    list = []
    for i in range(1,21):  # Loop through modes
        u = plucked_string(x, t, L, p[j], c, a, i)
        list.append(u)
        ax[j].plot(x, u , label = f'n = {i}') # Plot wave modes 
    r = np.array(list, dtype = object)
    ori = np.sum(r,axis = 0)

    ax[j].plot(x,ori, label = "Superposition Wave", linewidth = 2.5, color = 'k') # Plot superposition 
    ax[j].set_xlabel('x')
    ax[j].set_ylabel('Amplitude') 
    ax[j].set_title(f'Plucked at {p[j]}cm')   
    ax[j].scatter(4,0,marker="o",color='r',s=130, zorder=2,label = 'Bridge Pickup') # Bridge Pick-up
    ax[j].scatter(15,0,marker="o",color='b',s=130, zorder=2,label = 'Neck Pickup') # Neck pick-up
    ax[j].scatter(p[j],0,marker="x",color='k',s=130, zorder=2,label = 'Plucking Point') # Bridge Pick-up
    ax[j].text(-2.5,-0.1,'Bridge',fontsize=13)
    ax[j].text(62,-0.15,'Headstock',fontsize=13)    
    ax[j].legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax[j].grid()
