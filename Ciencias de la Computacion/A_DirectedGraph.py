
import networkx as nx
import matplotlib.pyplot as plt

Grafo = nx.DiGraph()
Grafo.add_node("A")      # add_node("n") agrega "n" como nodo del grafo
Grafo.add_node("B")
Grafo.add_node("C")

Grafo.add_edge("A","B")  # add_edge("e") agrega "e" como borde de un nodo
Grafo.add_edge("B","C")
Grafo.add_edge("A","C")
Grafo.add_edge("B","D")

Grafo.add_edge("B","A")  # add_edge("e") agrega "e" como borde de un nodo


nx.draw_circular(Grafo, node_size=50,width=1,with_labels=True)
plt.axis("equal")
plt.show()
