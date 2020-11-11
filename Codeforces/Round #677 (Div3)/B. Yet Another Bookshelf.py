#print(" ".join(map(str,array)))
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    first_one = last_one = -1
    zeroes = 0
    for i in range(n):
        if a[i] == 1:
            first_one = i
            break
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            last_one = i
            break
    for i in range(first_one+1, last_one):
        if a[i] == 0:
            zeroes += 1
    print(zeroes)
