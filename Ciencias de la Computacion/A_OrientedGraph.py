
import networkx as nx
import matplotlib.pyplot as plt

Grafo = nx.DiGraph()
Grafo.add_node("A")      
Grafo.add_node("B")
Grafo.add_node("C")

Grafo.add_edge("A","B")  
Grafo.add_edge("B","C")
Grafo.add_edge("A","C")
Grafo.add_edge("B","D")


nx.draw_circular(Grafo, node_size=50,width=1,with_labels=True)
plt.axis("equal")
plt.show()
