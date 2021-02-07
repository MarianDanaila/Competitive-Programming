import heapq
n, m = [int(s) for s in input().split(" ")]
graph = {}
for _ in range(m):
    u, v, w = [int(s) for s in input().split(" ")]
    if u not in graph:
        graph[u] = [[v, w]]
    else:
        graph[u].append([v, w])

    if v not in graph:
        graph[v] = [[u, w]]
    else:
        graph[v].append([u, w])

visited = [False] * n
dist = [float("inf")] * n
dist[0] = 0
heap = [[0, 0]]
while heap:
    value, node = heapq.heappop(heap)
    visited[node] = True
    if dist[node] < value:  # if we already found a better value
        continue
    if node not in graph:  # if we have directed graph
        continue
    for w, nxt_node in graph[node]:
        if visited[nxt_node]:
            continue
        if dist[node] + w < dist[nxt_node]:
            dist[nxt_node] = dist[node] + w
            heapq.heappush(heap, dist[nxt_node])
