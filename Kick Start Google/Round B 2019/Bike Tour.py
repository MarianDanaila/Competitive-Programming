t = int(input())
for k in range(1, t + 1):
    n = int(input())
    checkpoints = [int(s) for s in input().split(" ")]
    peak = 0
    for i in range(1, len(checkpoints)-1):
        if checkpoints[i] > checkpoints[i-1] and checkpoints[i] > checkpoints[i+1]:
            peak += 1

    print("Case #{}: {}".format(k, peak))