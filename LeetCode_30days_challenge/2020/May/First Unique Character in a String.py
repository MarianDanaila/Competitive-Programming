def firstUniqChar(s):
    dct = {}
    for i in range(len(s)):
        try:
            dct[s[i]][0] += 1
        except KeyError:
            dct[s[i]] = [1, i]
    for i in dct:
        if dct[i][0] == 1:
            return dct[i][1]
    return -1

print(firstUniqChar("leetcode"))