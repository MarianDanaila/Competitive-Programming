t = int(input())
for test in range(1, t+1):
    n = int(input())
    s = input()
    ans = [1]
    for i in range(1, n):
        if s[i] > s[i-1]:
            ans.append(ans[-1]+1)
        else:
            ans.append(1)
    print("Case #{}: {}".format(test, " ".join(map(str, ans))))
