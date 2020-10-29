# Problema e facuta bine doar ca infoarena nu ofera 100 pct din cauza MLE :(

from collections import deque
with open ("admitere-fmi-2016.in", "r") as fin:
    n, m, k = [int(s) for s in fin.readline().split(" ")]
    friends = [int(s) for s in fin.readline().split(" ")]
    graph = {}
    for i in range(1, 2*m, 2):
        if friends[i-1] not in graph:
            graph[friends[i-1]] = [friends[i]]
        else:
            graph[friends[i-1]].append(friends[i])

        if friends[i] not in graph:
            graph[friends[i]] = [friends[i-1]]
        else:
            graph[friends[i]].append(friends[i-1])
    #print(graph)
    with open("admitere-fmi-2016.out", "w") as fout:
        # punctul a
        output = [0] * n
        for key in graph:
            output[key-1] = len(graph[key])
        fout.write(" ".join(map(str, output)))
        fout.write('\n')
        # punctul b
        dct = {}
        removed = deque()
        #print(output)
        for i in range(n):
            if output[i] < k:
                removed.append(i+1)
        while removed:

            for _ in range(len(removed)):
                key = removed.popleft()
                output[key-1] = -1
                for friend in graph[key]:
                    if output[friend-1] != -1:
                        output[friend-1] -= 1
                        if output[friend-1] < k:
                            removed.append(friend)

        ans = []
        for i in range(len(output)):
            if output[i] >= k:
                ans.append(i+1)

        if len(ans) < 2:
            fout.write("NU")
        else:
            fout.write(" ".join(map(str, ans)))




