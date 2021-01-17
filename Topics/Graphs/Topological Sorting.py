# Approach 1 using modified DFS
nr_vertices, nr_edges = [int(s) for s in input().split(" ")]
graph = {}
for _ in range(nr_edges):
    v1, v2 = [int(s) for s in input().split(" ")]
    if v1 not in graph:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)


def topological_sort(v, visited, stack):
    visited[v] = True
    if v in graph:
        for nxt in graph[v]:
            if not visited[nxt]:
                topological_sort(nxt, visited, stack)
    stack.append(v)


visited = [False] * nr_vertices
stack = []
for i in range(nr_vertices):
    if not visited[i]:
        topological_sort(i, visited, stack)
print(stack[::-1])

# Approach 2 using Kahn's method
from collections import deque
nr_vertices, nr_edges = [int(s) for s in input().split(" ")]
in_degree = [0] * nr_vertices
graph = {}
for _ in range(nr_edges):
    v1, v2 = [int(s) for s in input().split(" ")]
    in_degree[v2] += 1
    if v1 not in graph:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)

dq = deque()
visited = 0
for i in range(len(in_degree)):
    if in_degree[i] == 0:
        dq.append(i)

while dq:
    curr = dq.popleft()
    visited += 1
    if curr in graph:
        for nxt in graph[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                dq.append(nxt)
if visited != nr_vertices:
    print("No topological sorting because cycle is found")
else:
    print("There exist a topological sorting")

