import networkx as nx
from task_1 import G

# Функція для знаходження шляхів за допомогою DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                stack.append((next_vertex, path + [next_vertex]))

# Функція для знаходження шляхів за допомогою BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))

# Виклик функцій для знаходження шляхів
start_node = 2
end_node = 7

dfs_paths_result = list(dfs_paths(G, start_node, end_node))
bfs_paths_result = list(bfs_paths(G, start_node, end_node))

# Виведення результатів
print("Шляхи, знайдені за допомогою DFS:")
for path in dfs_paths_result:
    print(path)

print("\nШляхи, знайдені за допомогою BFS:")
for path in bfs_paths_result:
    print(path)
