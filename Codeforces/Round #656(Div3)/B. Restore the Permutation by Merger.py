t = int(input())
for i in range(t):
    ans = ""
    length = int(input())
    hash = [1] * length
    p = [int(s) for s in input().split(" ")]
    for el in p:
        if hash[el-1] == 1:
            ans += str(el) + " "
            hash[el-1] = 0
    print(ans[:-1])


