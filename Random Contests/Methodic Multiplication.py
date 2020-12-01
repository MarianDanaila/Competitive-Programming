s1 = input()
s2 = input()
if s1 == '0' or s2 == '0':
    print('0')
else:
    cnt1 = 0
    for ch in s1:
        if ch == '(':
            cnt1 += 1
    cnt2 = 0
    for ch in s2:
        if ch == '(':
            cnt2 += 1
    cnt = cnt1*cnt2
    ans = [''] * (cnt*3 + 1)
    for i in range(0, 2*cnt, 2):
        ans[i] = 'S'
        ans[i+1] = '('
    ans[2*cnt] = '0'
    for i in range(2*cnt + 1, 3*cnt+1):
        ans[i] = ')'
    print("".join(ans))
