import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (перехрестя)
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])

# Додавання ребер (вулиць)
edges = [(1, 2, {'weight': 1}), (2, 3, {'weight': 3}), (3, 4, {'weight':5}), 
         (4, 5, {'weight': 2}), (5, 1, {'weight': 2}), (1, 3, {'weight': 1}), 
         (2, 4, {'weight': 2}), (3, 5, {'weight': 4}), (5, 6, {'weight': 2}), 
         (4, 6, {'weight': 3}), (5, 7, {'weight': 1}), (6, 7, {'weight': 3})]
G.add_edges_from(edges)


# Візуалізація графа
if __name__ == "__main__":
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
    plt.title("Мережа вулиць міста")
    plt.show()

    # Аналіз характеристик графа
    print("Кількість вершин:", G.number_of_nodes())
    print("Кількість ребер:", G.number_of_edges())
    print("Список вершин:", list(G.nodes()))
    print("Список ребер:", list(G.edges()))
    print("Ступінь вершин:", dict(G.degree()))
