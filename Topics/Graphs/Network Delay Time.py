import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
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
