t = int(input())
for _ in range(t):
    a, b, x, y, n = [int(s) for s in input().split(" ")]
    #cop_n = n
    if a-n >= x:
        min_a = a-n
        n1 = 0
    else:
        min_a = x
        n1 = n-(a-x)

    if b-n >= y:
        min_b = b-n
        n2 = 0
    else:
        min_b = y
        n2 = n-(b-y)

    if min_a <= min_b:
        print(min_a*max(y, b-n1))
    else:
        print(min_b*max(x, a-n2))

