t = int(input())
for test in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]
    intervals = []
    for _ in range(n):
        s, e = [int(s) for s in input().split(" ")]
        intervals.append([s, e])
    intervals.sort()
    counter = 0
    harvesting = 0
    i = 0
    for interval in intervals:
        s = interval[0]
        e = interval[1]
        harvesting = max(s, harvesting)
        if harvesting >= e:
            continue
        length = e-harvesting
        tmp = (length+k-1) // k
        counter += tmp
        harvesting += tmp * k
    print("Case #{}: {}".format(test, counter))
