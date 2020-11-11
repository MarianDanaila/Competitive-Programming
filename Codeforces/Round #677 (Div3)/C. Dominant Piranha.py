#print(" ".join(map(str,array)))
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    # check if there are dominant piranhas
    first_piranha = a[0]
    dominant = False
    for i in range(1, n):
        if a[i] != first_piranha:
            dominant = True
    if not dominant:
        print(-1)
    else:
        dominant_piranha = max(a)
        if a[0] > a[1] and a[0] == dominant_piranha:
            print(1)
        elif a[-1] > a[-2] and a[-1] == dominant_piranha:
            print(n)
        else:
            for i in range(1, n-1):
                if (a[i] > a[i-1] or a[i] > a[i+1]) and a[i] == dominant_piranha:
                    print(i+1)
                    break
