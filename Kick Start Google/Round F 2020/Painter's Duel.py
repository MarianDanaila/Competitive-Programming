t = int(input())
for test in range(1, t+1):
    s, r_a, p_a, r_b, p_b, c = [int(s) for s in input().split(" ")]
    pairs = []
    for _ in range(c):
        x, y = [int(s) for s in input().split(" ")]
        pairs.append([x, y])
    if c == 2:  # 12 cases
        print("Case #{}: {}".format(test, 0))
    if c == 1:  # 24 cases
        if pairs[0][0] == 2 and pairs[0][1] == 2:
            print("Case #{}: {}".format(test, 0))
        else:
            if r_b == 2 and p_b == 2:
                print("Case #{}: {}".format(test, -1))
            else:
                print("Case #{}: {}".format(test, 1))
    if c == 0:  # 12 cases
        if r_b == 2 and p_b == 2:
            print("Case #{}: {}".format(test, -1))
        elif r_a == 2 and p_a == 2:
            print("Case #{}: {}".format(test, 1))
        else:
            print("Case #{}: {}".format(test, 2))
