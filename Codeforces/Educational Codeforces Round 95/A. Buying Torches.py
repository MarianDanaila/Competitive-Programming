t = int(input())
for _ in range(t):
    x, y, k = [int(s) for s in input().split(" ")]
    sticks = k * (y+1)
    if (sticks - 1) % (x-1) == 0:
        print((sticks - 1) // (x-1) + k)
    else:
        print((sticks - 1) // (x-1) + k + 1)

