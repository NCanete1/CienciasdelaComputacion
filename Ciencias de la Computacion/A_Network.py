
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

pos={"A": (0.3, 0.2,), "B": (0.2, 0.5), "C": (0.1, 0.2), 
    "D": (0.2, 0.0)}

nx.draw(Grafo, pos,with_labels=True)
nx.draw_networkx_edge_labels(Grafo,pos,
    edge_labels={("B","C"): 1, 
                 ("A","B"): 2, 
                 ("A","C"): 3, 
                 ("B","D"): 5},label_pos=0.3,
    font_color='red'
)
plt.axis('off')
plt.show()
