import networkx as nx

from task_1 import G

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes()}
    shortest_paths[start] = 0
    visited = set()

    while len(visited) < len(graph.nodes()):
        current_node = None
        current_min_distance = float('inf')
        for node in set(shortest_paths.keys()) - visited:
            if shortest_paths[node] < current_min_distance:
                current_node = node
                current_min_distance = shortest_paths[node]

        visited.add(current_node)

        for neighbor, edge_data in graph[current_node].items():
            distance_to_neighbor = shortest_paths[current_node] + edge_data['weight']
            if distance_to_neighbor < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance_to_neighbor

    return shortest_paths

# Знаходження найкоротших шляхів для кожної вершини графа
shortest_paths = {}
for node in G.nodes():
    shortest_paths[node] = dijkstra(G, node)

# Виведення результатів
for node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи з вершини {node}:")
    for dest_node, distance in paths.items():
        print(f"  До вершини {dest_node}: {distance}")
