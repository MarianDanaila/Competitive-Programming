t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    sum_array = sum(a)
    if sum_array < n:
        print(1)
    else:
        print(sum_array - n)
