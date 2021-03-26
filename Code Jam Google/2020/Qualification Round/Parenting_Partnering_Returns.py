t = int(input())
for test in range(1, t + 1):
    ok = 1
    display = ""
    n = int(input())
    lst = [None] * n
    activities = []
    for i in range(n):
        temp = ([int(s) for s in input().split(" ")])
        temp.insert(0, i)
        activities.append(temp)

    c = 0
    j = 0
    activities.sort(key=lambda x: x[1])
    for i in activities:
        if i[1] >= c:
            c = i[2]
            lst[i[0]] = "C"
        elif i[1] >= j:
            j = i[2]
            lst[i[0]] = "J"
        else:
            print("Case #{}: {}".format(test, "IMPOSSIBLE"))
            ok = 0
            break
    if ok == 1:
        for i in lst:
            display += i
        print("Case #{}: {}".format(test, display))

