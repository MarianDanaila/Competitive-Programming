t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    l = [int(s) for s in input().split(" ")]
    positive_sum = 0
    negative_sum = 0
    unlocked = []
    for i in range(n):
        if l[i] == 0:
            unlocked.append(a[i])
    unlocked.sort()
    for i in range(n):
        if l[i] == 0:
            a[i] = unlocked[-1]
            unlocked.pop()
    out = ""
    for el in a:
        out += str(el) + ' '
    print(out[:-1])
