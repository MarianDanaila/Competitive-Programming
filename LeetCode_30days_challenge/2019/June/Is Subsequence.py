def isSubsequence(s, t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    index = 0
    for ch in t:
        if ch == s[index]:
            index += 1
            if index == len(s):
                return True
    return False

