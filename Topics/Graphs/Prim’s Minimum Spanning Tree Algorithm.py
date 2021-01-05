# Approach 1 using Matrix for graph representation
# Time-complexity: O(V^2)

nr_vertices, nr_edges = [int(s) for s in input().split(" ")]
graph = [[0]*nr_vertices for _ in range(nr_vertices)]
for _ in range(nr_edges):
    u, v, w = [int(s) for s in input().split(" ")]
    graph[u][v] = w
    graph[v][u] = w
key = [float("inf")] * nr_vertices
mst = [None] * nr_vertices
mst[0] = -1
key[0] = 0
mstSet = [False] * nr_vertices

for i in range(nr_vertices):
    minim = float("inf")
    for j in range(nr_vertices):
        if key[j] < minim and not mstSet[j]:
            minim = key[j]
            min_index = j
    mstSet[min_index] = True
    for j in range(nr_vertices):
        if 0 < graph[min_index][j] < key[j] and not mstSet[j]:
            key[j] = graph[min_index][j]
            mst[j] = min_index
print(mst)
min_cost = 0
for i in range(nr_vertices):
    min_cost += graph[mst[i]][i]
print(min_cost)

# Approach 2 using Adjacency List for graph representation
import heapq
nr_vertices, nr_edges = [int(s) for s in input().split(" ")]
graph = {}
for _ in range(nr_edges):
    u, v, w = [int(s) for s in input().split(" ")]
    if u in graph:
        graph[u].append([v, w])
    else:
        graph[u] = [[v, w]]

    if v in graph:
        graph[v].append([u, w])
    else:
        graph[v] = [[u, w]]

visited = set()
min_cost = 0
minHeap = [(0, 0)]
while minHeap:
    cost, vertex = heapq.heappop(minHeap)
    if vertex not in visited:
        min_cost += cost
        visited.add(vertex)
        for nxt, cost in graph[vertex]:
            if nxt not in visited:
                heapq.heappush(minHeap, (cost, nxt))
print(min_cost)
