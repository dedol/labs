from metro_min import graph
from iterators import Visited

def dfs_path(graph, node, final_node, output):
    global path_count, visited
    if node == final_node:
        path_count += 1
        if output:
            print(' -> '.join(x for x in visited.list()) + ' -> ' + final_node)
        return True

    visited.add(node)

    for c, neighbor in graph[node]:
        if not visited.has(neighbor):
            dfs_path(graph, neighbor, final_node, output)

    visited.remove(node)


if __name__ == '__main__':
    visited = Visited()
    path_count = 0

    dfs_path(graph, 'Красные Ворота (1)', 'Тверская (2)', output=False)
    print(path_count)

