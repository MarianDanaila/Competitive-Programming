class Solution:
    def makeConnected(self, n: int, connections):
        if len(connections) + 1 < n:
            return -1

        subsets = [[i, 0] for i in range(n)]

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

        for comp1, comp2 in connections:
            set1 = find(subsets, comp1)
            set2 = find(subsets, comp2)
            if set1 != set2:
                union(subsets, set1, set2)
        components = 0
        for i in range(n):
            if subsets[i][0] == i:
                components += 1
        return components - 1
