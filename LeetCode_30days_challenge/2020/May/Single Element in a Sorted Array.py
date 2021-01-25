def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        if low == high:
            return nums[low]
        mid = low + (high - low) // 2
        if mid % 2 == 0:
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        else:
            if nums[mid] == nums[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))