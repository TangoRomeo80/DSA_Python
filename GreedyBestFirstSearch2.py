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


def gbs(sNode, gNode):
    visited = {}
    priority = PriorityQueue()
    for node in graph.keys():
        visited[node] = False

    startingPoint = sNode
    visited[startingPoint] = True
    priority.put((hSLD[startingPoint], startingPoint))

    while not priority.empty():
        u = priority.get()[1]
        for v in graph[u].keys():
            if not visited[v]:
                if v == gNode:
                    return v
                else:
                    visited[v] = True
                    priority.put((hSLD[v], v))

    return None


if gbs('S', 'G'):
    print(gbs('S', 'G'))

else:
    print('Failure')
