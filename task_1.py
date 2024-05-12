import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (перехрестя)
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])

# Додавання ребер (вулиць)
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4), (3, 5), (5, 6), (4, 6), (5, 7), (6, 7)]
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
