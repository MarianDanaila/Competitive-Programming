from collections import deque
with open('sate.in', 'r') as fin:
    n, m, x, y = [int(s) for s in fin.readline().split(' ')]
    graph = {}
    for _ in range(m):
        i, j, d = [int(s) for s in fin.readline().split(' ')]
        if i not in graph:
            graph[i] = [[j, d]]
        else:
            graph[i].append([j, d])

        if j not in graph:
            graph[j] = [[i, -d]]
        else:
            graph[j].append([i, -d])

    visited = [False] * (n+1)
    dist = [0] * (n+1)
    q = deque()
    q.append(x)
    visited[x] = True
    found = False
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            neigh = i[0]
            distance = i[1]
            if not visited[neigh]:
                visited[neigh] = True
                dist[neigh] = dist[curr] + distance
                q.append(neigh)

                if neigh == y:
                    with open('sate.out', 'w') as fout:
                        fout.write(str(dist[y]))
                    found = True
                    break
        if found:
            break
