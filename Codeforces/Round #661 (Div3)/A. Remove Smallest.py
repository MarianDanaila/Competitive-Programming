t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort()
    ok = True
    if n == 1:
        print("YES")
    else:
        for i in range(n-1):
            if abs(a[i]-a[i+1]) > 1:
                print("NO")
                ok = False
                break

        if ok:
            print("YES")