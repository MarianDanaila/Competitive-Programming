def hIndex(citations):
    if len(citations) == 0 or (len(citations) == 1 and citations[0] == 0):
        return 0
    l = 0
    r = len(citations) - 1
    ans = 0
    while l <= r:
        mid = l + (r - l) // 2
        if citations[mid] == len(citations) - mid:
            return citations[mid]
        elif citations[mid] > len(citations) - mid:
            ans = len(citations) - mid
            r = mid - 1
        else:
            l = mid + 1
    return ans