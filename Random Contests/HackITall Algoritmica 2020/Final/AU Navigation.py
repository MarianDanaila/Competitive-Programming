n = int(input())
a = [int(s) for s in input().split(" ")]
occ = []
cnt = 1
for i in range(1, n):
    if a[i] == a[i-1]:
        cnt += 1
    else:
        occ.append([cnt, a[i-1]])
        cnt = 1
occ.append([cnt, a[-1]])
#print(occ)
ans = 0
while len(occ) > 0:
    maxim = 0
    element = -1
    for i in range(len(occ)):
        if occ[i][0] > maxim:
            maxim = occ[i][0]
            index = i
    ans += 1
    #print(index)
    occ.pop(index)
    #print(occ)
    if index != 0 and index != len(occ):
        if occ[index][1] == occ[index-1][1]:
            occ[index-1][0] += occ[index][0]
            occ.pop(index)
print(ans)


