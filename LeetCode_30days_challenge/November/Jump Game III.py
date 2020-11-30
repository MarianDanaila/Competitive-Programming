from collections import deque


class Solution:
    def canReach(self, A, i):
        if A[i] == 0:
            return True
        n = len(A)
        graph = {}
        for idx in range(n):
            if A[idx] == 0:
                continue
            temp = []
            if idx-A[idx] >= 0:
                temp.append(idx-A[idx])
            if idx+A[idx] < n:
                temp.append(idx+A[idx])
            graph[idx] = temp
        dq = deque()
        dq.append(i)
        visited = [False] * n
        while dq:
            for _ in range(len(dq)):
                curr = dq.popleft()
                for neigh in graph[curr]:
                    if not visited[neigh]:
                        if A[neigh] == 0:
                            return True
                        dq.append(neigh)
                        visited[neigh] = True
        return False
