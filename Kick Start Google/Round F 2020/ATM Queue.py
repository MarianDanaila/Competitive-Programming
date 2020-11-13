t = int(input())
for t in range(1, t+1):
    n, x = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]
    for i in range(n):
        if a[i] % x == 0:
            a[i] = [a[i] // x, i+1]
        else:
            a[i] = [a[i] // x + 1, i+1]

    a.sort(key=lambda x: (x[0], x[1]))
    out = ""
    for el in a:
        out += str(el[1]) + " "
    print("Case #{}: {}".format(t, out[:-1]))
