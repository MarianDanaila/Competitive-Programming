from collections import deque


def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)


t = int(input())
for test in range(1, t + 1):
    n, q = [int(s) for s in input().split(" ")]
    graph = {}
    for _ in range(n - 1):
        x, y, l, a = [int(s) for s in input().split(" ")]
        if x not in graph:
            graph[x] = [[y, l, a]]
        else:
            graph[x].append([y, l, a])

        if y not in graph:
            graph[y] = [[x, l, a]]
        else:
            graph[y].append([x, l, a])
    # process all queries

    answer = []
    for _ in range(q):
        c, w = [int(s) for s in input().split(" ")]
        dq = deque()
        dq.append([c, 0])
        visited = set()
        visited.add(c)
        while dq:
            city, gcd = dq.popleft()
            for neighbor, l, a in graph[city]:
                new_gcd = gcd
                if neighbor not in visited:
                    if w >= l:
                        new_gcd = find_gcd(a, gcd)
                    dq.append([neighbor, new_gcd])
                    visited.add(neighbor)
                    if neighbor == 1:
                        answer.append(new_gcd)
                        dq.clear()
                        break

    print("Case #{}: {}".format(test, " ".join(map(str, answer))))
