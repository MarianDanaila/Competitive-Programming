from collections import deque
with open("output.txt", "w") as fout:
    t = int(input())
    for test in range(1, t + 1):
        n = int(input())
        c = [int(s) for s in input().split(" ")]
        if n == 1:
            fout.write("Case #{}: {}".format(test, c[0]))
            fout.write("\n")
        else:
            graph = {}
            for _ in range(n - 1):
                a, b = [int(s) for s in input().split(" ")]
                if a not in graph:
                    graph[a] = [b]
                else:
                    graph[a].append(b)

                if b not in graph:
                    graph[b] = [a]
                else:
                    graph[b].append(a)
            # print(graph)
            dq = deque()
            dq.append([1, c[0], set()])
            leaf_road = []
            leaf_gold = 0
            visited = set()
            visited.add(1)
            while dq:
                cave, gold, road = dq.popleft()
                # print(cave, gold, road)
                child = False
                for next_cave in graph[cave]:
                    if next_cave not in visited:
                        child = True
                        next_road = road.copy()
                        next_road.add(next_cave)
                        dq.append([next_cave, gold + c[next_cave - 1], next_road])
                        visited.add(next_cave)
                if not child:  # it is a leaf
                    if gold > leaf_gold:
                        leaf_gold = gold
                        leaf_road = road.copy()

            for cave in leaf_road:
                graph.pop(cave)

            visited = set()
            dq = deque()
            dq.append([1, c[0]])
            visited.add(1)
            leaf2_gold = 0
            while dq:
                cave, gold = dq.popleft()
                child = False
                for next_cave in graph[cave]:
                    if next_cave not in leaf_road and next_cave not in visited:
                        child = True
                        dq.append([next_cave, gold + c[next_cave - 1]])
                        visited.add(next_cave)
                if not child:  # it is a leaf
                    if gold > leaf2_gold:
                        leaf2_gold = gold

            fout.write("Case #{}: {}".format(test, leaf2_gold + leaf_gold - c[0]))
            fout.write("\n")