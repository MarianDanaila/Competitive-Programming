from collections import deque
t = int(input())
for test in range(1, t+1):
    s, e = input().split(" ")
    found = False
    target = int(e, 2)
    dq = deque()
    visited = set()
    dq.append(int(s, 2))
    visited.add(int(s, 2))
    operations = 0
    while dq:
        len_dq = len(dq)
        for _ in range(len_dq):
            curr = dq.popleft()
            if curr == target:
                print("Case #{}: {}".format(test, operations))
                found = True
                break
            multiplied = curr * 2
            negative = 0
            curr = bin(curr)[2:]
            for ch in curr:
                negative *= 2
                if ch == '0':
                    negative += 1
            if multiplied not in visited and multiplied < 65536:
                visited.add(multiplied)
                dq.append(multiplied)
            if negative not in visited and multiplied < 65535:
                visited.add(negative)
                dq.append(negative)
        operations += 1
        if found:
            break
    if not found:
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))