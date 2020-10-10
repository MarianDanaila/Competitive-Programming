t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    zeroes = 0
    ones = 0
    output = ""
    for num in a:
        if num == 0:
            zeroes += 1
        else:
            ones += 1
    if zeroes >= n // 2:
        print(zeroes)
        print('0 ' * zeroes)
    else:
        print(ones-ones % 2)
        print('1 ' * (ones - ones % 2))
