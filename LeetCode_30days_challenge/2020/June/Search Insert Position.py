def searchInsert(nums, target):
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

print(searchInsert([1,3,5,6], 2))