from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(subsets, v):
            if subsets[v][0] != v:
                subsets[v][0] = find(subsets, subsets[v][0])
            return subsets[v][0]

        def union(subsets, v1, v2):
            if subsets[v1][1] < subsets[v2][1]:
                subsets[v1][0] = v2
            elif subsets[v1][1] > subsets[v2][1]:
                subsets[v2][0] = v1
            else:
                subsets[v2][0] = v1
                subsets[v1][1] += 1

        n = len(points)
        subsets = [[i, 0] for i in range(n)]
        graph = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append([i, j, dist])

        i = e = 0
        graph.sort(key=lambda x: x[2])
        min_cost = 0
        while e < n - 1:
            u, v, cost = graph[i]
            i += 1
            set_u = find(subsets, u)
            set_v = find(subsets, v)
            if set_u != set_v:
                e = e + 1
                union(subsets, set_u, set_v)
                min_cost += cost
        return min_cost
