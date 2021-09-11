from collections import deque

with open("output.txt", "w") as fout:
    t = int(input())
    for test in range(1, t + 1):
        s = input()
        k = int(input())
        graph = {}
        for _ in range(k):
            edge = input()
            a, b = edge[0], edge[1]
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)
        min_seconds = float("inf")
        replaces = {}
        for i in range(65, 91):
            visited = set()
            target = chr(i)
            dq = deque()
            seconds = 1
            if target in graph:
                dq.append(target)
                visited.add(target)
            while dq:
                len_dq = len(dq)
                for _ in range(len_dq):
                    curr = dq.popleft()
                    if curr in graph:
                        for neighbor in graph[curr]:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                dq.append(neighbor)
                                replaces[neighbor] = seconds
                seconds += 1

            total_seconds = 0
            for ch in s:
                if ch != target:
                    if ch in replaces:
                        total_seconds += replaces[ch]
                    else:
                        total_seconds = float("inf")
                        break
            min_seconds = min(min_seconds, total_seconds)
            replaces.clear()

        if min_seconds == float("inf"):
            min_seconds = -1
        fout.write("Case #{}: {}".format(test, min_seconds))
        fout.write("\n")
