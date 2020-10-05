n = int(input())
a = [int(s) for s in input().split(" ")]
if n == 1:
    print(1, 1)
    print(-a[0])
    print(1, 1)
    print(0)
    print(1, 1)
    print(0)
else:
    print(1, 1)
    print(-a[0])
    print(1, n)
    second = "0 "
    for i in range(2, n+1):
        second += str(-n*a[i-1]) + " "
    print(second[:-1])
    print(2, n)
    third = ""
    for i in range(2, n+1):
        third += str((n-1)*a[i-1]) + " "
    print(third[:-1])
