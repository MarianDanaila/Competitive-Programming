with open("sortaret.in", 'r') as fin:
    n, m = [int(s) for s in fin.readline().split(" ")]
    graph = {}
    for _ in range(m):
        x, y = [int(s) for s in fin.readline().split(" ")]
        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]

    def topologicalSort(vertex, visited, stack):
        visited[vertex-1] = True

        if vertex in graph:
            for neigh in graph[vertex]:
                if not visited[neigh-1]:
                    topologicalSort(neigh, visited, stack)

        stack.append(vertex)

    visited = [False] * n
    stack = []
    for i in range(1, n+1):
        if not visited[i-1]:
            topologicalSort(i, visited, stack)
with open("sortaret.out", "w") as fout:
    fout.write(" ".join(map(str, stack[::-1])))
