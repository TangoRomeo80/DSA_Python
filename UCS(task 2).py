from queue import PriorityQueue

graph = {
    'S': {'A': 2, 'B': 1, },
    'A': {'C': 2, 'D': 3},
    'B': {'D': 4, 'E': 4},
    'C': {'G': 4},
    'D': {'G': 4},
    'E': {},
    'G': {}
}


def ucs(sNode, gNode):
    visited = {}
    distance = {}
    parent = {}

    priority = PriorityQueue()
    for node in graph.keys():
        visited[node] = False
        parent[node] = None
        distance[node] = -1

    startingPoint = sNode
    visited[startingPoint] = True
    distance[startingPoint] = 0
    priority.put((0, startingPoint))

    while not priority.empty():
        u = priority.get()[1]
        if u == gNode:
            break
        visited[u] = True
        for v in graph[u].keys():
            if not visited[v]:
                parent[v] = u
                distance[v] = distance[u] + graph[u][v]
                priority.put((distance[v], v))

    print(priority)
    g = gNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    print(path)
    print(distance[gNode])


ucs('S', 'G')
