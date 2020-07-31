t = int(input())
for _ in range(t):
    n = int(input())
    if n < 31:
        print("NO")
    else:
        print("YES")
        if n == 36:
            print("5 6 10 15")
        if n == 40:
            print("15 14 10 1")
        if n == 44:
            print("6 7 10 21")
        if n != 36 and n != 40 and n != 44:
            print("6 10 14 "+ str(n-30))