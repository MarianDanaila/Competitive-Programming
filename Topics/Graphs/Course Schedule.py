# Kahn Algorithm
from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
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
        while dq:
            curr = dq.popleft()
            visited += 1
            if curr in graph:
                for nxt in graph[curr]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        dq.append(nxt)

        return visited == numCourses
