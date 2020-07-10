t = int(input())
for test in range(1, t + 1):
    diff = []
    n, k = [int(s) for s in input().split(" ")]
    workouts = [int(s) for s in input().split(" ")]
    for i in range(len(workouts) - 1):
        diff.append(workouts[i + 1] - workouts[i])
    while k > 0:
        maxim = max(diff)
        diff.append(maxim // 2)
        diff.append(round(maxim / 2 + 0.1))
        diff.remove(maxim)
        k -= 1
    print("Case #{}: {}".format(test, max(diff)))

# solved only for test set 1