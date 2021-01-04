t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split(" ")]
    bottom = [int(s) for s in input().split(" ")]
    left = [int(s) for s in input().split(" ")]
    counter = 0
    for b in bottom:
        if b in left:
            counter += 1
    print(counter)