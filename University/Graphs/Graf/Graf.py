from collections import deque
with open("graf.in", "r") as fin:
    n, m, x, y = map(int, fin.readline().split(" "))
    graph = {}
    # build the graph
    for _ in range(m):
        a, b = map(int, fin.readline().split(" "))
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    q = deque()
    q.append([x, 1, {1}])
    stop = False

    visited = [False] * n
    visited[x-1] = True
    ans = []
    while q:
        level = []
        for _ in range(len(q)):
            vertex, length, path = q.popleft()
            level.append(vertex)

            for connected in graph[vertex]:
                if visited[connected-1]:
                    continue
                if connected == y:  # valid path
                    if stop:

                        ans = ans.intersection(path)
                    else:
                        stop = True
                        ans = path

                if not stop:

                    path.add(connected)
                    q.append([connected, length+1, path.copy()])
                    path.remove(connected)

        for vertex in level:
            visited[vertex-1] = True
        if stop:
            break
    ans.add(y)
out = []
for key in ans:
    out.append(key)
out.sort()
with open("graf.out", "w") as fout:
    fout.write(" ".join(map(str, out)))