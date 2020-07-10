t = int(input())
for test in range(1, t + 1):
    n, d = [int(s) for s in input().split(" ")]
    routes = [int(s) for s in input().split(" ")]
    maxim = d
    for i in range(len(routes)-1, -1, -1):
        maxim = maxim - (maxim % routes[i])
    print("Case #{}: {}".format(test, maxim))
