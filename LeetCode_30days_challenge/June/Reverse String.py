def reverseString(s):
    if len(s) % 2 == 0:
        limit = len(s) // 2 + 1
    else:
        limit = len(s) //2
    for i in range(limit):
        s[i], s[-i-1] = s[-i-1], s[i]
    return s
