from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            in_degree[a] += 1
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)

        dq = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)

        order = []
        while dq:
            curr = dq.popleft()
            order.append(curr)
            if curr in graph:
                for nxt in graph[curr]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        dq.append(nxt)

        if len(order) == numCourses:
            return order
        return []
