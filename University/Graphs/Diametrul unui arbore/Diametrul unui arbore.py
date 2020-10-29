from collections import deque

with open('darb.in', 'r') as fin:
    n = int(fin.readline())
    graph = {}
    # build graph
    for _ in range(n-1):
        a, b = [int(s) for s in fin.readline().split(" ")]
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    def bfs(node):
        visited = [False] * n
        distance = [-1] * n
        distance[node-1] = 1
        q = deque()
        q.append(node)
        visited[node-1] = True
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                if not visited[neigh-1]:
                    visited[neigh-1] = True
                    distance[neigh-1] = distance[node-1] + 1
                    q.append(neigh)
        diameter = 0
        for i in range(n):
            if distance[i] > diameter:
                diameter = distance[i]
                node_index = i+1
        return [node_index, diameter]

    node, diameter = bfs(a)

    ans = bfs(node)

    with open('darb.out', 'w') as fout:
        fout.write(str(ans[1]))

