from collections import deque
with open("bfs.in", 'r') as fin:
    n, m, s = [int(s) for s in fin.readline().split(" ")]
    graph = {}
    found = False
    for _ in range(m):
        x, y = [int(s) for s in fin.readline().split(" ")]
        if x == y:
            found = True
        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]

    visited = [False] * n
    q = deque()
    q.append(s)
    visited[s-1] = True
    distances = [0] * n
    while q:
        curr = q.popleft()
        if curr not in graph:
            continue
        #print(graph[curr])
        for neigh in graph[curr]:
            if not visited[neigh-1]:
                distances[neigh-1] = distances[curr-1] + 1
                visited[neigh-1] = True
                q.append(neigh)
    for i in range(n):
        if distances[i] == 0:
            distances[i] = -1
    if found:
        distances[s-1] = 0
    with open('bfs.out', 'w') as fout:
        fout.write(" ".join(map(str, distances)))
