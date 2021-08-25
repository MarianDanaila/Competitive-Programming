from math import ceil
modulo = 10 ** 9 + 7
tests = int(input())
for t in range(1, tests + 1):
    n, k = [int(s) for s in input().split(" ")]
    s = input()
    # check last palindrome +/- 1
    ans = 0
    for i in range(ceil(n / 2)):
        power = (n - 1) // 2 - i
        ans += (ord(s[i]) - 97) * (pow(k, power, modulo))
    last = False
    for i in range(n // 2 - 1, -1, -1):
        if s[i] < s[n - i - 1]:
            last = True
            break
        elif s[i] > s[n - i - 1]:
            break
    if last and n > 1:
        ans += 1
    print("Case #{}: {}".format(t, ans % modulo))
