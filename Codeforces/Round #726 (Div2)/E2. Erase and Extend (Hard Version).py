from math import ceil

n, k = [int(s) for s in input().split(" ")]
s = input()
prefix_idx = 0
idx = n - 1
for i in range(1, n):
    if s[i] == s[prefix_idx]:
        if idx == n - 1:
            idx = i - 1
        prefix_idx += 1
    elif s[i] < s[prefix_idx]:
        prefix_idx = 0
        idx = n - 1
    else:
        if idx == n - 1:
            idx = i - 1
        break

multiply = ceil(k / (idx + 1))
print((s[:idx + 1] * multiply)[:k])
