# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        #BFS solution
        if not node:
            return node
        # create a new node
        new_node = Node(node.val)
        # create a dictionary to store the visited nodes
        visited = {node: new_node}
        # create a queue to store the nodes to be visited
        queue = [node]
        # start BFS traversal
        while queue:
            # pop a node from the front of the queue
            n = queue.pop(0)
            # iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # create a new neighbor
                    new_neighbor = Node(neighbor.val)
                    # add the new neighbor to the visited dictionary
                    visited[neighbor] = new_neighbor
                    # add the neighbor to the queue
                    queue.append(neighbor)
                # add the new neighbor to the neighbors of the new node
                visited[n].neighbors.append(visited[neighbor])
        return new_node