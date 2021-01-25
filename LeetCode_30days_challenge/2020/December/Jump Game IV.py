from collections import deque


class Solution:
    def minJumps(self, arr):
        dct = {}
        n = len(arr)
        if n == 1:
            return 0
        for i in range(n):
            if arr[i] in dct:
                dct[arr[i]].append(i)
            else:
                dct[arr[i]] = [i]

        visited = [False] * n
        visited[0] = True
        dq = deque()
        dq.append(0)
        steps = 0
        while dq:
            steps += 1
            for _ in range(len(dq)):
                index = dq.popleft()
                if arr[index] in dct:
                    for nxt in dct[arr[index]]:
                        if not visited[nxt]:  # if it is not visited
                            if nxt == n-1:  # we found the index
                                return steps
                            visited[nxt] = True  # mark as visited
                            dq.append(nxt)  # add to queue
                    dct.pop(arr[index])
                if index > 0:
                    if not visited[index-1]:
                        visited[index-1] = True
                        dq.append(index-1)
                if not visited[index+1]:
                    if index+1 == n-1:
                        return steps
                    visited[index+1] = True
                    dq.append(index+1)
        return steps
