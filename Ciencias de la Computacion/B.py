
import networkx as nx
import matplotlib.pyplot as plt

Grafo = nx.Graph()
Grafo.add_node(1)      
Grafo.add_node(2) 
Grafo.add_node(3)      
Grafo.add_node(4) 
Grafo.add_node(5)      
Grafo.add_node(6) 

Grafo.add_edge(1,5)  
Grafo.add_edge(1,2)
Grafo.add_edge(2,3)
Grafo.add_edge(2,5)
Grafo.add_edge(3,4)  
Grafo.add_edge(4,5)
Grafo.add_edge(4,6)



pos={1: (0.7, 0.4), 2: (0.6, 0.2), 3: (0.3, 0.1), 
    4: (0.2, 0.4), 5: (0.5, 0.5), 6: (0.0, 0.55)}

nx.draw(Grafo, pos,with_labels=True)
plt.axis("equal")
plt.show()
