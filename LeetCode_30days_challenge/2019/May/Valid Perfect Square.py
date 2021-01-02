def isPerfectSquare(num):
    if num == 1:
        return True
    l = 1
    r = num // 2
    while l <= r:
        mid = l + (r-l) // 2
        if mid*mid == num:
            return True
        elif mid*mid < num:
            l = mid+1
        else:
            r = mid-1
    return False
print(isPerfectSquare(144))