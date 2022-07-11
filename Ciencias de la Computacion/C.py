
import networkx as nx
import matplotlib.pyplot as plt

Grafo = nx.Graph()
G = nx.DiGraph()
Gr = nx.DiGraph()

Grafo.add_node(0) 
Grafo.add_node(1)      
Grafo.add_node(2) 
Grafo.add_node(3)      
Grafo.add_node(4) 
Grafo.add_node(5)      
Grafo.add_node(6) 
Grafo.add_node(7)      
Grafo.add_node(8) 
Grafo.add_node(9)      



Grafo.add_edge(0,1)  
Grafo.add_edge(0,6)
Grafo.add_edge(1,4)
Grafo.add_edge(1,6)
Grafo.add_edge(1,9)  
Grafo.add_edge(2,4)
Grafo.add_edge(2,6)
Grafo.add_edge(3,4)
Grafo.add_edge(3,8)
Grafo.add_edge(4,9)
Grafo.add_edge(4,5)
Grafo.add_edge(7,8)
Grafo.add_edge(7,9)

G.add_edge(0,8)
Gr.add_edge(3,5)

pos={1: (0.7, 0.4,), 2: (0.9, 0.3), 3: (0.9, 0.2), 
    4: (0.8, 0.1), 5: (0.6, 0.0), 6: (0.3, 0.1), 
    7: (0.1, 0.2), 8: (0.1, 0.34), 9: (0.3, 0.4), 
    0: (0.5, 0.5)}

nx.draw(Grafo, pos,with_labels=True)
nx.draw_networkx_edges(G, pos,connectionstyle="arc3,rad=0.2")
nx.draw_networkx_edges(Gr, pos,connectionstyle="arc3,rad=-0.4")
plt.show()
