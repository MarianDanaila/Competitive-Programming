t = int(input())
for _ in range(t):
    n, x, y = [int(s) for s in input().split(" ")]
    minim = 1000000001
    out = []
    cop_n = n
    ans = ""
    if n == 2:
        print(x, y)
    else:
        diff = y-x
        i = diff
        while i > 0:
            if diff % i == 0:  # i is divisor
                a = []
                curr = y
                n = cop_n
                while curr > x and n > 0:
                    a.append(curr)
                    n -= 1
                    curr -= i

                if curr == x and n > 0:
                    a.append(curr)
                    n -= 1
                    curr -= i
                    while n > 0 and curr > 0:
                        a.append(curr)
                        n -= 1
                        curr -= i
                    curr = y+i
                    while n > 0:
                        a.append(curr)
                        n -= 1
                        curr += i

                    if max(a) < minim:
                        minim = max(a)
                        out = a
            i -= 1
        for el in out:
            ans += str(el) + " "
        print(ans[:-1])


