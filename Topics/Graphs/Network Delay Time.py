# Dijkstra
import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = [[v, w]]
            else:
                graph[u].append([v, w])
        dist = [float("inf")] * n
        min_heap = [[0, k]]
        while min_heap:
            time, v = heapq.heappop(min_heap)
            if time < dist[v-1]:
                dist[v-1] = time
                if v in graph:
                    for nxt, w in graph[v]:
                        heapq.heappush(min_heap, [time+w, nxt])
        if max(dist) < float("inf"):
            return max(dist)
        else:
            return -1


# Bellman Ford
class Solution:
    def networkDelayTime(self, times, n, k):
        dist = [float("inf")] * n
        dist[k-1] = 0
        for _ in range(n-1):
            for u, v, w in times:
                u -= 1
                v -= 1
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        if max(dist) < float("inf"):
            return max(dist)
        else:
            return -1


# Floyd Warshall
class Solution:
    def networkDelayTime(self, times, n, k):
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in times:
            dist[u-1][v-1] = w

        for a in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][a]+dist[a][j])

        if max(dist[k-1]) < float("inf"):
            return max(dist[k-1])
        else:
            return -1
