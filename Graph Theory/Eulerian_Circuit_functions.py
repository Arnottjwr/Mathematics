###########################################
from Eulerian_functions import Eulerian_circuit_1, Eulerian_circuit_2, Eulerian_circuit_3, all_positive_degree_vertices_connected
# Examples 
import networkx as nx
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

G1 = nx.Graph([{0,1},{0,4},{0,5},{0,6},{1,2},{2,6},{2,3},{2,5},{3,4},{4,5},{4,6},{5,6}])
G2 = nx.Graph([{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 3}, {0, 3}])
G3 = nx.Graph([{0,1},{1,2},{2,3},{3,4},{4,1},{1,5},{5,0}])
G4 = nx.Graph([{0, 1}, {1, 2},{0,2},{0,4},{0,3},{3,4}])

nx.draw_networkx(G1, ax=axs[0, 0], pos=nx.circular_layout(G1), node_color="g", edgecolors="k")
nx.draw_networkx(G2, ax=axs[0, 1],pos=nx.circular_layout(G2), node_color="g", edgecolors="k")
nx.draw_networkx(G3, ax=axs[1, 0],pos=nx.circular_layout(G3), node_color="g", edgecolors="k")
nx.draw_networkx(G4, ax=axs[1, 1],pos=nx.circular_layout(G4), node_color="g", edgecolors="k")

axs[0, 0].set_title('Eulerian Circuit 1')
axs[0, 1].set_title('Eulerian Circuit 2')
axs[1, 0].set_title('Eulerian Circuit 3')
axs[1, 1].set_title('All Vertices Connected')


descriptions = [
    (f'Graph with Eulerian circuit {Eulerian_circuit_1(G1)}'),
    (f'Graph with Eulerian circuit {Eulerian_circuit_2(G2)}'),
    (f'Graph with Eulerian circuit {Eulerian_circuit_3(G3)}'),
    (f'Connected Component: {all_positive_degree_vertices_connected(G4)}')]

for i, ax in enumerate(axs.flatten()):
    ax.text(0.5, -0.3, descriptions[i], transform=ax.transAxes, ha='center', fontsize=10, wrap=True)
    ax.axis('on')

plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.show()
