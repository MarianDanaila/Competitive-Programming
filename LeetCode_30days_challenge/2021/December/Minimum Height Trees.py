from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in edges:
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = {b}
            if b in graph:
                graph[b].add(a)
            else:
                graph[b] = {a}

        leaves = deque()
        centroids = n
        for i in range(n):
            if i not in graph or len(graph[i]) == 1:  # it's a leaf
                leaves.append(i)
        while centroids > 2:
            nr_leaves = len(leaves)
            centroids -= nr_leaves
            for _ in range(nr_leaves):
                leaf = leaves.popleft()
                neighbour = graph[leaf].pop()
                graph[neighbour].remove(leaf)
                if len(graph[neighbour]) == 1:
                    leaves.append(neighbour)
        return list(leaves)
