n, m = [int(s) for s in input().split(" ")]
graph = {}
for _ in range(m):
    v1, v2 = [int(s) for s in input().split(' ')]
    if v1 not in graph:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)


def find(subsets, vertex):
    if subsets[vertex][0] != vertex:
        subsets[vertex][0] = find(subsets, subsets[vertex][0])
    return subsets[vertex][0]


def union(subsets, u, v):
    if subsets[u][1] > subsets[v][1]:
        subsets[v][0] = u
    elif subsets[u][1] < subsets[v][1]:
        subsets[u][0] = v
    else:
        subsets[v][0] = u
        subsets[u][1] += 1


cycle = False
subsets = [[i, 0] for i in range(n)]
for vertex in graph:
    x = find(subsets, vertex)
    for connected_vertex in graph[vertex]:
        y = find(subsets, connected_vertex)
        if x == y:
            print("DA")
            cycle = True
            break
        else:
            union(subsets, x, y)
            print(subsets)
    if cycle:
        break
if not cycle:
    print("NU")

# LeetCode Helper Class For DSU


class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
