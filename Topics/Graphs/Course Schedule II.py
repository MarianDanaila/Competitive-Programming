from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        in_degree = [0] * numCourses
        for p1, p2 in prerequisites:
            in_degree[p1] += 1
            if p2 not in graph:
                graph[p2] = [p1]
            else:
                graph[p2].append(p1)

        dq = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                dq.append(i)

        visited = 0
        topological_sort = []
        while dq:
            curr = dq.popleft()
            visited += 1
            topological_sort.append(curr)
            if curr in graph:
                for nxt in graph[curr]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        dq.append(nxt)

        if visited == numCourses:
            return topological_sort
        else:
            return []
