import math 
import matplotlib.pyplot as plt 
import networkx as nx 
 
def generate_bloom_lattice(rings=3): 
    G = nx.Graph() 
    PHI = 1.61803398875 
    base_freq = 528.0 
    G.add_node(0, pos=(0, 0), freq=base_freq, label="Genesis (528Hz)") 
    node_id = 1 
    for r in range(1, rings + 1): 
        radius = r * PHI 
        num_points = 6 * r 
        for i in range(num_points): 
            angle = (2 * math.pi / num_points) * i 
            x = radius * math.cos(angle) 
            y = radius * math.sin(angle) 
            freq = base_freq * (PHI ** r) 
            G.add_node(node_id, pos=(x, y), freq=freq, label=f"R{r}-{i}") 
            G.add_edge(0, node_id) 
            node_id += 1 
    return G 
 
if __name__ == "__main__": 
    print("Initializing Castleberry Bloom Lattice...") 
    lattice = generate_bloom_lattice(rings=2) 
    pos = nx.get_node_attributes(lattice, 'pos') 
    plt.figure(figsize=(8, 8)) 
    nx.draw(lattice, pos, with_labels=False, node_size=300, node_color='purple', edge_color='gray') 
    plt.title("Castleberry Hexagonal Bloom Lattice (528 Hz Baseline)") 
    plt.savefig("bloom_lattice.png") 
    print("Lattice rendered and saved as 'bloom_lattice.png'.") 
