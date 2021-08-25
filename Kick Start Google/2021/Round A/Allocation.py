t = int(input())
for test in range(1, t + 1):
    n, b = [int(s) for s in input().split(" ")]
    houses =[int(s) for s in input().split(" ")]
    houses.sort()
    counter = 0
    for i in houses:
        if b >= i:
            counter += 1
            b -= i
        else:
            break
    print("Case #{}: {}".format(test, counter))