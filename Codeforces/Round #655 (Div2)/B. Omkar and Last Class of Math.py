from math import sqrt
t = int(input())
for i in range(t):
    ok = 1
    n = int(input())
    if n % 2 == 0:
        print(n//2, n//2)
    else:
        for j in range(2, int(sqrt(n))+1):
            if n % j == 0:
                print(n // j, n - n//j)
                ok = 0
                break
        if ok:
            print(1, n-1)