from metro import graph
from iterators import Queue, Visited

def bfs_shortest(start_node, end_node):
    queue = Queue([(0, start_node, [])])
    visited = Visited()

    while queue.has_next():
        (cost, node, path) = queue.pop(0)
        if not visited.has(node):
            visited.add(node)
            path = path + [node]

            if node == end_node:
                print('Наикратчайший маршрут: \t')
                print('\n'.join(f'\t{station}' for station in path))
                print(f'Потребуется времени: {cost} мин')

            for c, neighbour in graph[node]:
                if not visited.has(neighbour):
                    queue.add((cost+c, neighbour, path))

if __name__ == "__main__":
    bfs_shortest('Красные Ворота (1)', 'Тверская (2)')