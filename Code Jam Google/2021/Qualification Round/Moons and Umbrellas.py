t = int(input())
for test in range(1, t+1):
    x, y, s = input().split(" ")
    x = int(x)
    y = int(y)

    cost = 0
    first = None
    for ch in s:
        if ch == 'C':
            if first is None:
                first = 'C'
            else:
                if first != ch:
                    cost += y
                    first = 'C'
        elif ch == 'J':
            if first is None:
                first = 'J'
            else:
                if first != ch:
                    cost += x
                    first = 'J'
    print("Case #{}: {}".format(test, cost))
