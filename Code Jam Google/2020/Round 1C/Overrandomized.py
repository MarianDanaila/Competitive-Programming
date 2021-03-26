from operator import itemgetter
t = int(input())
for test in range(1, t + 1):
    u = int(input())
    output = [None] * 10
    info = []
    display = ""
    for i in range(10000):
        line = input().split(" ")
        info.append([int(line[0]), line[1]])
    info = sorted(info, key=itemgetter(0))
    dct = {}
    for i in info:
        if i[0] < 10:
            try:
                if dct[i[1]] == 1:
                    continue
            except KeyError:
                output[i[0]] = i[1]
                dct[i[1]] = 1
        if len(str(i[0])) == len(i[1]) and i[0] == 10:
            output[0] = i[1][1]
    for i in output:
        display += i
    print("Case #{}: {}".format(test, display))



   # Solved only for test set 1
