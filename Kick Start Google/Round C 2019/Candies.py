t = int(input())
for test in range(1, t + 1):
    n, q = [int(s) for s in input().split(" ")]
    arr = [int(s) for s in input().split(" ")]
    score = 0
    for i in range(q):
        line = input().split(" ")
        a = int(line[1])
        b = int(line[2])
        if line[0] == 'U':
            arr[a-1] = b
        else:
            suma = 0
            ok = 1
            for j in range(a-1, b):
                if ok % 2 == 0:
                    suma -= ok*arr[j]
                else:
                    suma += ok*arr[j]
                ok += 1
            score += suma
    print("Case #{}: {}".format(test, score))
