# the following lines are reserved for imports
#
#

import collections


def bfs(prblm, S, G):

    visited, queue = set(), collections.deque([S])
    visited.add(S)
    path = []

    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for neighbour in prblm[vertex]:
            if neighbour == G:
                print(path)
                return
            elif neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


prblm = {'S': {'A': 2, 'B': 1},
         'A': {'C': 2, 'D': 3},
         'B': {'D': 4, 'E': 4},
         'C': {'G': 4},
         'D': {'G': 4},
         'E': {},
         'G': {}
         }
print("Following is Breadth First Traversal: ")
bfs(prblm, 'S', 'G')
