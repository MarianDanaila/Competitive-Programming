#print(" ".join(map(str,array)))
from sys import stdout
n = int(input())
ans = [-1] * n
mx = 0
for i in range(1, n):
    print("?", mx+1, i+1)
    stdout.flush()
    ans1 = int(input())
    print("?", i+1, mx+1)
    stdout.flush()
    ans2 = int(input())
    if ans1 > ans2:
        ans[mx] = ans1
        mx = i
    else:
        ans[i] = ans2
ans[mx] = n
print("! ")
print(" ".join(map(str, ans)))
    