t = int(input())
for _ in range(t):
    n = int(input())
    dct = {}
    ok = True
    for i in range(n):
        s = input()
        for ch in s:
            try:
                if dct[ch] > 0:
                    dct[ch] += 1
            except KeyError:
                dct[ch] = 1
    for el in dct:
        if dct[el] % n != 0:
            print("NO")
            ok = False
            break
    if ok:
        print("YES")
