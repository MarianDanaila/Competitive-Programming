def firstBadVersion(n):
    l = 0
    r = n
    while l <= r:
        m = l + (r-l) // 2
        if isBadVersion(m):
            r = m-1
            ans = m
        else:
            l = m+1
    return ans
