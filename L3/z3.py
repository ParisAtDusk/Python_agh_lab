import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq

def dijkstra(graph, start):
    priority_queue = []
    hq.heappush(priority_queue, (0, start))  # (distance, node)
    
    # Store the shortest distances to each node
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    
    # Store the shortest path tree
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = hq.heappop(priority_queue)
        
        # Skip processing if we have already found a shorter path
        if current_distance > shortest_distances[current_node]:
            continue
        
        # Check the adjacent nodes
        for adj_node, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path is found, update the shortest distance
            if distance < shortest_distances[adj_node]:
                shortest_distances[adj_node] = distance
                previous_nodes[adj_node] = current_node
                hq.heappush(priority_queue, (distance, adj_node))
    
    return shortest_distances, previous_nodes


def display_graph(graph):
    G = nx.Graph()
    plt.figure(figsize=(8, 6))
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

        # Use an automatic layout
    positions = nx.spring_layout(G)  

    # Draw the graph
    
    if positions is None:
        positions = nx.spring_layout(G)  # First graph gets the positions
    else:
        # You could use the same layout or customize as needed
        nx.spring_layout(G, pos=positions)  # Reuse the same positions
    nx.draw(
        G, 
        pos=positions,  # Use the auto-generated positions
        with_labels=True, 
        node_color='lightblue', 
        node_size=2000, 
        font_size=15,
        font_color='black',
        edge_color='gray'
    )

    # Draw edge labels for weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels, font_size=12)
    plt.show()

def recreate_path(paths, start, end):
    path = []
    current_node = end
    
    # Follow the path backward until we reach the start (None)
    while current_node is not None:
        path.append(current_node)
        current_node = paths[current_node]
    
    # Reverse the path to get it from start to end
    path.reverse()
    
    return path

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 4},
    'C': {'A': 2, 'B': 1, 'D': 2, 'E': 5},
    'D': {'B': 4, 'C': 2, 'E': 1, 'F':1},
    'E': {'C': 5, 'D': 1, 'F':2},
    'F': {'E': 2, 'D': 1}
}

start_node = 'A'
distances, paths = dijkstra(graph, start_node)
print("Shortest distances from ", start_node, " node to:", distances)
print("Paths:", paths)

# Recreate a graph from A - F with the shortest path
print("Shortest path from A to F: ", recreate_path(paths,'A', 'F'))

display_graph(graph)

