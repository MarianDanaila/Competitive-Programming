# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        clone = {node: Node(node.val)}

        def dfs(node):
            for neigh in node.neighbors:
                if neigh not in clone:
                    clone[neigh] = Node(neigh.val)
                    dfs(neigh)
                clone[node].neighbors.append(clone[neigh])

        dfs(node)
        return clone[node]
