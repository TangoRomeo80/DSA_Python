class Queue:

    def __init__(self, pop_index=0):
        self.queue = []
        self.pop_index = pop_index

    def append(self, item):
        self.queue.append(item)

    def sortAppend(self, item, f):
        self.queue.append(item)
        self.queue.sort(key=f)

    def extend(self, items):
        self.queue.extend(items)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(self.pop_index)
        else:
            raise Exception('FIFOQueue is empty')

    def printQueue(self):
        print("Frontier Status After Adding .............")
        print([items.state for items in self.queue])

    def __len__(self):
        return len(self.queue)

    def __contains__(self, item):
        return item in self.queue


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

heuristicSLD = {
    'Arad': 366,
    'Bucharest': 161,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 0,
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


class graphProblem:

    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + self.graph[state1][state2]


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, graphProblem):
        return [self.child_node(graphProblem, action)
                for action in graphProblem.actions(self.state)]

    def child_node(self, graphProblem, action):
        next_state = graphProblem.result(self.state, action)
        return Node(next_state, self, action,
                    graphProblem.path_cost(self.path_cost, self.state, action, next_state))

    def path(self):
        node, path_back = self, []

        while node:
            path_back.append(node)
            node = node.parent

        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]


def graph_search(problem, pop_index):
    node = Node(problem.initial)

    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)

    explored = set()

    frontier.append(node)

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        print("Parent: ", node.state,
              "Childs: ", [child.state for child in node.expand(problem)])

        explored.add(node.state)

        for child in node.expand(problem):
            if problem.goal_test(child.state): return child
            if child.state not in explored and child not in frontier: frontier.append(child)

    return None


gp = graphProblem('Zerind', 'Eforie', graph)


def best_first_search(problem, f, pop_index=0):
    node = Node(problem.initial)
    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)
    frontier.sortAppend(node, f)

    explored = Queue()

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        if problem.goal_test(node.state): return node
        explored.append(node)

        for child in node.expand(problem):
            if child not in explored and child not in frontier:
                frontier.sortAppend(child, f)

    return None


def GBFS(problem):
    return best_first_search(problem, lambda node: heuristicSLD[node.state])


goalNode = GBFS(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)
print("=======================================")
print()