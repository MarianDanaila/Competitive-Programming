from math import sqrt
t = int(input())
for test in range(1, t + 1):
    z = int(input())
    target = int(sqrt(z))
    first = second = third = -1
    for i in range(target, target - 565, -1):
        prime = True
        for d in range(2, int(sqrt(i) + 1)):
            if i % d == 0:
                prime = False
                break
        if prime:
            if second == -1:
                second = i
            else:
                first = i
                break

    for i in range(target + 1, target + 283):
        prime = True
        for d in range(2, int(sqrt(i)) + 1):
            if i % d == 0:
                prime = False
                break
        if prime:
            third = i
            break

    if second * third <= z:
        print("Case #{}: {}".format(test, second * third))
    else:
        print("Case #{}: {}".format(test, first * second))
