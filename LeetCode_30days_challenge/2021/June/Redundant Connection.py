from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        subsets = [[i, 0] for i in range(n)]

        def find(v):
            # print(v)
            if subsets[v][0] != v:
                subsets[v][0] = find(subsets[v][0])
            return subsets[v][0]

        def union(v1, v2):
            if subsets[v1][1] < subsets[v2][1]:
                subsets[v1][0] = v2
            elif subsets[v1][1] > subsets[v2][1]:
                subsets[v2][0] = v1
            else:
                subsets[v1][0] = v2
                subsets[v2][1] += 1

        for edge in edges:
            v1, v2 = edge[0] - 1, edge[1] - 1
            v1_set = find(v1)
            v2_set = find(v2)
            if v1_set == v2_set:
                return [v1 + 1, v2 + 1]
            else:
                union(v1_set, v2_set)
