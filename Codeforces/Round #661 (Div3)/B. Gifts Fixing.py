t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    b = [int(s) for s in input().split(" ")]
    min_a = min(a)
    min_b = min(b)
    moves = 0
    for i in range(n):
        diff_a = a[i]-min_a
        diff_b = b[i]-min_b
        moves += max(diff_a, diff_b)
    print(moves)
