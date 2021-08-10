t = int(input())
for _ in range(t):
    n = int(input())
    h = [int(s) for s in input().split(" ")]
    h.sort()
    min_diff = float("inf")
    idx = -1
    for i in range(1, n):
        if h[i] - h[i - 1] < min_diff:
            min_diff = h[i] - h[i - 1]
            idx = i - 1
    first, second = h[idx], h[idx + 1]
    h.pop(idx)
    h.pop(idx)
    h.insert(0, first)
    h.append(second)
    idx = -1

    for i in range(1, n - 1):
        if h[i] >= h[0]:
            idx = i
            break

    if idx == -1:
        print(" ".join(map(str, h)))
    else:
        ans = [h[0]]
        for i in range(idx, n - 1):
            ans.append(h[i])
        for i in range(1, idx):
            ans.append(h[i])
        ans.append(h[-1])
        print(" ".join(map(str, ans)))
