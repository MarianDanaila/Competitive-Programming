t = int(input())
for test in range(1, t+1):
    n, a, b, c = [int(s) for s in input().split(" ")]
    if n == 1:
        print("Case #{}: {}".format(test, 1))
    elif a+b-c > n:
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
    else:
        stop = False
        buildings = [0] * n
        if c > 1:
            copy_c = c
            for i in range(a-c):
                buildings[i] = 1
            for i in range(n-1, n-1-(b-c), -1):
                buildings[i] = 1

            left = a-c
            right = n-1-(b-c)
            if c % 2 == 1:
                buildings[left] = 2
                c -= 1
                left += 1
            while c > 0:
                buildings[left] = 2
                buildings[right] = 2
                left += 1
                right -= 1
                c -= 2

            remaining = n-a-b+copy_c

            while remaining > 0:
                buildings[left] = 1
                left += 1
                remaining -= 1

        else:
            if a+b-c == n:
                for i in range(a-c):
                    buildings[i] = 1
                for i in range(n-1, n-1-(b-c), -1):
                    buildings[i] = 1
                buildings[a-c] = 2
            elif a > 1 or b > 1:
                #print("DA")
                for i in range(a-1):
                    buildings[i] = 2
                for i in range(n-1, n-1-(b-1), -1):
                    buildings[i] = 2
                left = a-1
                right = n-1-(b-1)

                buildings[(left+right)//2] = 3
                for i in range(n):
                    if buildings[i] == 0:
                        buildings[i] = 1
            else:
                print("Case #{}: {}".format(test, "IMPOSSIBLE"))
                stop = True

        if not stop:
            print("Case #{}: {}".format(test, " ".join(map(str, buildings))))


