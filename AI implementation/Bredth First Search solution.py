from queue import Queue

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

    while not adjacent_queue.empty():
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


bfs('Arad', 'Bucharest')
