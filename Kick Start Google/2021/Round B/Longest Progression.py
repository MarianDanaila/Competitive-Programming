t = int(input())
for test in range(1, t + 1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    diffs = []
    prev_diff = a[1] - a[0]
    cnt = 1
    for i in range(2, n):
        if a[i] - a[i - 1] == prev_diff:
            cnt += 1
        else:
            diffs.append([prev_diff, cnt])
            prev_diff = a[i] - a[i - 1]
            cnt = 1
    diffs.append([prev_diff, cnt])
    max_length = 0
    for diff, cnt in diffs:
        max_length = max(max_length, cnt + 2)
    len_diffs = len(diffs)
    max_length = min(max_length, n)
    for i in range(1, len_diffs):
        target = (diffs[i][0] + diffs[i - 1][0]) / 2
        curr_length = 0
        if 2 <= i < len_diffs - 1 and target == diffs[i - 2][0] == diffs[i + 1][0]:
            max_length = max(max_length, diffs[i - 2][1] + diffs[i + 1][1] + 3)
        elif i >= 2 and target == diffs[i - 2][0]:
            max_length = max(max_length, diffs[i - 2][1] + 3)
        elif i < len_diffs - 1 and target == diffs[i + 1][0]:
            max_length = max(max_length, diffs[i + 1][1] + 3)
    print("Case #{}: {}".format(test, max_length))
