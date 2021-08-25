from math import sqrt
t = int(input())
for test in range(1, t+1):
    g = int(input())
    limit = int((-1 + sqrt(8 * g + 1)) // 2)
    counter = 0
    for d in range(1, limit + 1):
        if g / d - int(g / d) == 0.5:
            counter += 1
        elif g % d == 0:
            if d % 2 == 1:
                counter += 1

    print("Case #{}: {}".format(test, counter))
