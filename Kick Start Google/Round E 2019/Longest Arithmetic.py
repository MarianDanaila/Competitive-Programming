t = int(input())
for test in range(1, t + 1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    count = 2
    diff = a[1] - a[0]
    out = 2
    for i in range(2, n):
        if a[i] - a[i-1] == diff:
            count += 1
        else:
            out = max(out, count)
            diff = a[i] - a[i-1]
            count = 2
    out = max(out, count)
    print("Case #{}: {}".format(test, out))