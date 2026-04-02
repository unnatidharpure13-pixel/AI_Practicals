# Semantic Network using Dictionary
def semantic_network():
    network = {}  # dictionary to store relations
    n = int(input("Enter number of relations: "))

    for i in range(n):
        print(f"\nEnter details for relation {i+1}:")
        subject = input("Enter Subject: ")
        relation = input("Enter Relation (e.g., ISA, HAS): ")
        obj = input("Enter Object: ")

        # Add to dictionary
        if subject not in network:
            network[subject] = []
        network[subject].append((relation, obj))

    print("\n--- Semantic Network Representation ---")
    for subject in network:
        for (relation, obj) in network[subject]:
            print(f"{subject} ---> {relation} ----> {obj}")

    return network


# Run program and get network data
network_data = semantic_network()

# Visualization code
import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges from the network data
for subject, relations in network_data.items():
    G.add_node(subject)
    for relation, obj in relations:
        G.add_node(obj)
        G.add_edge(subject, obj, label=relation)

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, k=0.8)  # Position nodes using force-directed algorithm

nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20, width=1.5)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=9)

plt.title('Semantic Network Diagram', size=15)
plt.axis('off')  # Hide axes
plt.show()