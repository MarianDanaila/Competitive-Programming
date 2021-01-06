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
