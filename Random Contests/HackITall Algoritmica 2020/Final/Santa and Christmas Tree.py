n, k = [int(s) for s in input().split(" ")]
p = [int(s) for s in input().split(" ")]
c = [int(s) for s in input().split(" ")]
s = [int(k) for k in input().split(" ")]
set_s = set(s)
#print(p,c,s, set_s)
from collections import deque
graph = {}
for i in range(2, n+1):
    if i not in graph:
        graph[i] = [p[i-2]]
    else:
        graph[i].append(p[i-2])

    if p[i-2] not in graph:
        graph[p[i-2]] = [i]
    else:
        graph[p[i-2]].append(i)

#print(graph)
ans = 0
if 1 in set_s:
    preffered = True
    k -= 1
    ans += c[0]
else:
    preffered = False
dq = deque()
dq.append([1, c[0], preffered])
visited = [False] * n
visited[0] = True
special = False
while dq:
    node, cost, preffered = dq.popleft()
    #print(node, cost)

    for connected_node in graph[node]:
        if not visited[connected_node-1]:  # if not visited
            visited[connected_node-1] = True  # it's visited now
            if not preffered:
                if cost == -1:
                    cost = max(cost, c[connected_node-1])
                else:
                    if c[connected_node-1] != -1:
                        cost = min(cost, c[connected_node-1])
            if connected_node in set_s:
                #print("TERMINAL")
                #print(connected_node, cost)

                if cost == -1:
                    special = True
                    print(-1)
                    break
                else:
                    if not preffered:
                        ans += cost
                    #print(ans)
                    dq.append([connected_node, cost, preffered])
            else:
                dq.append([connected_node, cost, preffered])
    if special:
        break

if not special:
    print(ans)
