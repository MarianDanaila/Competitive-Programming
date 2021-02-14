from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = set()
            graph[u].add(v)

            if v not in graph:
                graph[v] = set()

            graph[v].add(u)

        for i in range(1, n + 1):
            if i not in graph:
                graph[i] = set()

        degree = float("inf")

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                for k in range(j + 1, n + 1):
                    if j in graph[i] and k in graph[i] and k in graph[j]:
                        degree = min(degree, len(graph[i]) + len(graph[j]) + len(graph[k]) - 6)
        if degree == float("inf"):
            return -1
        return degree
