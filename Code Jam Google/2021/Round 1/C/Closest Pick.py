t = int(input())
for test in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]
    sold = [int(s) for s in input().split(" ")]
    sold.sort()
    max_diff = 0
    for i in range(1, n):
        max_diff = max(max_diff, sold[i] - sold[i - 1] - 1)
    diff = [0]
    if sold[0] != 1:
        diff[0] = sold[0] - 1
    for i in range(1, n):
        diff.append((sold[i] - sold[i - 1]) // 2)
    diff.append(0)
    if sold[-1] != k:
        diff[-1] = k - sold[-1]

    diff.sort()
    fav = diff[-1] + diff[-2]

    print("Case #{}: {}".format(test, max(max_diff, fav) / k))
