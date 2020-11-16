t = int(input())
for test in range(1, t+1):
    s = input()
    split = s.split("START")[:-1]
    ans = 0
    for i in range(len(split)):
        word = split[i]
        cnt = 0
        for j in range(len(word) - 3):
            if word[j:j + 4] == 'KICK':
                cnt += 1
        ans += cnt*(len(split)-i)
    print("Case #{}: {}".format(test, ans))