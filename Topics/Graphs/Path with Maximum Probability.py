import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        m = len(edges)
        for i in range(m):
            a, b = edges[i]
            p = succProb[i]
            if a not in graph:
                graph[a] = [[b, p]]
            else:
                graph[a].append([b, p])

            if b not in graph:
                graph[b] = [[a, p]]
            else:
                graph[b].append([a, p])
        if start not in graph:
            return 0
        heap = [[-1, start]]
        visited = [False] * n
        visited[start] = True
        p = [-1] * n
        p[start] = 1
        while heap:
            prob, curr = heapq.heappop(heap)
            prob = -prob
            if curr == end:
                return p[curr]
            if p[curr] > prob:
                continue
            for nxt, w in graph[curr]:
                if visited[nxt]:
                    continue
                if p[curr] * w > p[nxt]:
                    p[nxt] = p[curr] * w
                    heapq.heappush(heap, [-p[nxt], nxt])
        return 0
