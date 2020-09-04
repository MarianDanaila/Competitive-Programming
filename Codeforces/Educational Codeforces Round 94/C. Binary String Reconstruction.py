t = int(input())
for _ in range(t):
    s = input()
    x = int(input())
    n = len(s)
    w = ['1'] * n
    bad = False
    ans = ""
    for i in range(n):
        if s[i] == '0':
            if i-x >= 0:
                w[i-x] = '0'
            if i + x < n:
                w[i+x] = '0'
    for i in range(n):
        one = True
        second = True
        if i-x >= 0:
            if w[i-x] == '1':
                one = True
            else:
                one = False
        else:
            one = False
        if i + x < n:
            if w[i+x] == '1':
                second = True
            else:
                second = False
        else:
            second = False

        if one or second:
            if s[i] != '1':
                print(-1)
                bad = True
                break
        if one is False and second is False:
            if s[i] != '0':
                print(-1)
                bad = True
                break
    if not bad:
        for ch in w:
            ans += ch
        print(ans)