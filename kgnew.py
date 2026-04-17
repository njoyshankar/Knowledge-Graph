import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.DiGraph()

# Add relationships
G.add_edge("Elon Musk", "Tesla", relation="FOUNDED")
G.add_edge("Tesla", "USA", relation="LOCATED_IN")

# Print relationships
print("\nRelationships:\n")
for u, v, data in G.edges(data=True):
    print(f"{u} --({data['relation']})--> {v}")

# Draw graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

plt.show()