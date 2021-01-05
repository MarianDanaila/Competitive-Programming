# Approach 1: Kruskal's Algorithm
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        subsets = [[i, 0] for i in range(n)]

        def find(v):
            if subsets[v][0] != v:
                subsets[v][0] = find(subsets[v][0])
            return subsets[v][0]

        def union(v1, v2):
            if subsets[v1][1] < subsets[v2][1]:
                subsets[v1][0] = v2
            elif subsets[v1][1] > subsets[v2][1]:
                subsets[v2][0] = v1
            else:
                subsets[v1][0] = v2
                subsets[v2][1] += 1

        # create graph
        graph = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                graph.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        graph.sort(key=lambda x: x[2])

        min_cost = 0
        e = 0
        i = 0
        while e < n - 1:
            u, v, w = graph[i]
            set_u = find(u)
            set_v = find(v)
            if set_u != set_v:
                e += 1
                min_cost += w
                union(set_u, set_v)
            i += 1
        return min_cost


# Approach 2: Prim's Algorithm
import heapq


class Solution:
    def minCostConnectPoints(self, points):
        graph = {}
        n = len(points)
        if n == 1:
            return 0
        for i in range(n - 1):
            point1 = points[i]
            for j in range(i + 1, n):
                point2 = points[j]
                manhattan = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                if i not in graph:
                    graph[i] = [[j, manhattan]]
                else:
                    graph[i].append([j, manhattan])

                if j not in graph:
                    graph[j] = [[i, manhattan]]
                else:
                    graph[j].append([i, manhattan])
        visited = set()
        min_cost = 0
        min_heap = [[0, 0]]
        while min_heap:
            cost, point = heapq.heappop(min_heap)
            if point not in visited:
                visited.add(point)
                min_cost += cost
                for nxt, cost in graph[point]:
                    if nxt not in visited:
                        heapq.heappush(min_heap, [cost, nxt])
        return min_cost
