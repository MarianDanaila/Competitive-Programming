t = int(input())
for test in range(1, t + 1):
    line = input().split(" ")
    x = int(line[0])
    y = int(line[1])
    m = line[2]
    ok = 1
    for i in range(len(m)):
        if m[i] == 'N':
            y += 1
        if m[i] == 'S':
            y -= 1
        if m[i] == 'E':
            x += 1
        if m[i] == 'W':
            x -= 1
        if abs(x)+abs(y) <= i+1:
            print("Case #{}: {}".format(test, i+1))
            ok = 0
            break
    if ok:
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
