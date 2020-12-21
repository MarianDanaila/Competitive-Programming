k, a, b = [int(s) for s in input().split(" ")]
ans = 0
from collections import deque
dq = deque()
visited = [False] * (k+1)
maxim = -1
while dq:
    curr = dq.popleft()
    maxim = max(maxim, curr)
    if 0 <= curr+a <= k:
        if not visited[curr+a]:
            visited[curr+a] = True
            ans += k+1-maxim
            maxim = curr+a


    if 0 <= curr-b <= k:
        if not visited[curr-b]:
            visited[curr-b] = True
            ans += k+1-maxim
print(ans)
