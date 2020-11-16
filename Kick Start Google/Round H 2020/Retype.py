t = int(input())
for test in range(1, t+1):
    n, k, s = [int(s) for s in input().split(" ")]
    minutes = k - 1
    option1 = minutes + 1 + n
    option2 = minutes + (k-s) + (n-s+1)
    #print(option1, option2)
    print("Case #{}: {}".format(test, min(option1, option2)))
