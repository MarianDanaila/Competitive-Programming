# Time-complexity: O(E logE) or O(E logV)

# Union and Find Functions
def find(subsets, v):
    if subsets[v][0] != v:
        subsets[v][0] = find(subsets, subsets[v][0])
    return subsets[v][0]


def union(subsets, v1, v2):
    if subsets[v1][1] < subsets[v2][1]:
        subsets[v1][0] = v2
    elif subsets[v1][1] > subsets[v2][1]:
        subsets[v2][0] = v1
    else:
        subsets[v1][0] = v2
        subsets[v2][1] += 1


nr_vertices, nr_edges = [int(s) for s in input().split(" ")]
graph = []
subsets = [[i, 0] for i in range(nr_vertices)]
for _ in range(nr_edges):
    u, v, w = [int(s) for s in input().split(" ")]
    graph.append([u, v, w])

mst = []
i = 0
e = 0
graph.sort(key=lambda x: x[2])
min_cost = 0

while e < nr_vertices-1:
    u, v, w = graph[i]
    i += 1
    set_u = find(subsets, u)
    set_v = find(subsets, v)
    if set_u != set_v:
        e = e+1
        mst.append([u, v, w])
        union(subsets, set_u, set_v)
        min_cost += w
print(min_cost)
