def canJump(nums):
    maxim = 0
    for i in range(len(nums)-1):
        if nums[i] == 0 and maxim == 0:
            return False
        if nums[i] > maxim:
            maxim = nums[i]
        maxim -= 1
    return True

print(canJump([3,2,1,0,4]))