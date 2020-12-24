class Solution:
    def findCircleNum(self, M) -> int:
        n = len(M)
        subsets = [[i, 0] for i in range(n)]
        graph = {}
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i] = [j]

        def find(subsets, vertex):
            if subsets[vertex][0] != vertex:
                subsets[vertex][0] = find(subsets, subsets[vertex][0])
            return subsets[vertex][0]

        def union(subsets, v1, v2):
            if subsets[v1][1] > subsets[v2][1]:
                subsets[v2][0] = v1
            elif subsets[v1][1] < subsets[v2][1]:
                subsets[v1][0] = v2
            else:
                subsets[v2][0] = v1
                subsets[v1][1] += 1

        for v in graph:
            for connected in graph[v]:
                set_v = find(subsets, v)
                set_connected = find(subsets, connected)
                if set_v != set_connected:
                    union(subsets, set_v, set_connected)
                    n -= 1
        return n
