from queue import Queue

graph = {
    'S': {'A': 2, 'B': 1, },
    'A': {'C': 2, 'D': 3},
    'B': {'D': 4, 'E': 4},
    'C': {'G': 4},
    'D': {'G': 4},
    'E': {},
    'G': {}
}


def bfs(sNode, gNode):
    visited = {}
    distance = {}
    parent = {}

    adjacent_queue = Queue()
    for node in graph.keys():
        visited[node] = False
        parent[node] = None
        distance[node] = -1

    starting_point = sNode
    visited[starting_point] = True
    distance[starting_point] = 0
    adjacent_queue.put(starting_point)

    u = adjacent_queue.get()
        for v in graph[u].keys():
            if not visited[v]:
                if v == gNode:
                    parent[v] = u
                    distance[v] = distance[u] + graph[u][v]
                    break
                else:
                    visited[v] = True
                    parent[v] = u
                    distance[v] = distance[u] + graph[u][v]
                    adjacent_queue.put(v)

    g = gNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    print(path)
    print(distance[gNode])


bfs('S', 'G')
