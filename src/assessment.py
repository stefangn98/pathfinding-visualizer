import networkx as nx
from networkx.drawing.nx_pylab import draw_networkx
import numpy as np
import matplotlib.pyplot as plt

graph = {'a': ['j', 'h', 'i', 'k'],
         'l': ['e', 'c', 'b', 'k'],
         'f': ['e', 'h', 'c'],
         'h': ['a', 'i', 'b', 'f'],
         'd': ['e', 'j', 'b', 'g'],
         'g': ['c', 'j', 'd'],
         'b': ['k', 'h', 'e', 'j', 'd', 'l'],
         'c': ['l', 'i', 'g', 'k', 'f'],
         'k': ['b', 'e', 'c', 'a', 'l'],
         'e': ['d', 'l', 'b', 'k', 'f'],
         'i': ['h', 'c', 'a'],
         'j': ['a', 'd', 'b', 'g']}


G = nx.MultiGraph()
G.add_nodes_from(graph.keys())

for key in graph.keys():
    for value in graph[key]:
        G.add_edge(key, value)

pos = nx.spring_layout(G)

draw_networkx(G, pos)

plt.axis("off")
plt.show()
