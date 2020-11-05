class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n <= 2:
            return [i for i in range(n)]
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]

            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                for neigh in graph[leaf]:
                    graph[neigh].remove(leaf)
                    if len(graph[neigh]) == 1:
                        new_leaves.append(neigh)

            leaves = new_leaves
        return leaves
