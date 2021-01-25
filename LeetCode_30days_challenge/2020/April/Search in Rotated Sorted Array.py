def search(nums, target):
    l = 0
    r = len(nums)-1
    while l <= r:
        m = l + (r-l) // 2
        if nums[m] == target:
            return m
        am_big = nums[m] >= nums[0]
        target_big = target >= nums[0]
        if am_big == target_big:
            if target > nums[m]:
                l = m+1
            else:
                r = m-1
        else:
            if am_big:
                l = m+1
            else:
                r = m-1
    return -1
print(search([1, 3], 3))