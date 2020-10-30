from collections import deque
with open('dfs.in', 'r') as fin:
    n, m = [int(s) for s in fin.readline().split(' ')]
    graph = {}
    for _ in range(m):
        x, y = [int(s) for s in fin.readline().split(' ')]
        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]

        if y in graph:
            graph[y].append(x)
        else:
            graph[y] = [x]
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            q = deque()
            q.append(i+1)
            while q:
                curr = q.popleft()
                if curr not in graph:
                    break
                for neigh in graph[curr]:
                    if not visited[neigh-1]:
                        q.append(neigh)
                        visited[neigh-1] = True
    with open('dfs.out', 'w') as fout:
        fout.write(str(cnt))

