from queue import PriorityQueue

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211, 'Urziceni': 85},
    'Craiova': {'Drobeta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'RimnicuVilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'RimnicuVilcea': 80, 'Fagaras': 99},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}

hSLD = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi' : 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'RimnicuVilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def a_star(sNode, gNode):
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
    priority.put((hSLD[startingPoint], startingPoint))

    while not priority.empty():
        u = priority.get()[1]
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
                    priority.put((hSLD[v], v))

    g = gNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    print(f'Path to destination: {path}')
    print(f'Cost of reaching the destination: {distance[gNode]}')


a_star('Arad', 'Bucharest')

