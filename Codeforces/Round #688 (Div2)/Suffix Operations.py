t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    ans = 0
    for i in range(2, n + 1):
        ans += abs(a[i] - a[i - 1])
    print(ans)

    mx = max(abs(a[2] - a[1]), abs(a[n] - a[n - 1]))
    for i in range(2, n):
        mx = max(mx, abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i]) - abs(a[i + 1] - a[i - 1]))
    print(ans - mx)
