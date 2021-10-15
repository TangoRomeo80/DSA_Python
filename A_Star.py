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

hSLD = {
    'S': 6,
    'A': 0,
    'B': 6,
    'C': 4,
    'D': 1,
    'E': 10,
    'G': 0
}


def a_star(sNode, gNode):
    visited = {}
    distance = {}

    priority = PriorityQueue()
    for node in graph.keys():
        visited[node] = False
        distance[node] = -1

    startingPoint = sNode
    visited[startingPoint] = True
    distance[startingPoint] = 0
    priority.put((hSLD[startingPoint], startingPoint))

    while not priority.empty():
        u = priority.get()[1]
        for v in graph[u].keys():
            if not visited[v]:
                if v == gNode:
                    return v
                else:
                    visited[v] = True
                    distance[v] = distance[u] + graph[u][v]
                    priority.put((hSLD[v] + distance[v], v))

    return None


if a_star('S', 'G'):
    print(a_star('S', 'G'))

else:
    print('Failure')
