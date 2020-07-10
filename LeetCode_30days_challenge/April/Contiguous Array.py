def findMaxLength(nums):
    dct = {}
    if len(nums) == 0:
        return 0
    curr_sum = 0
    maxsize = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1
        curr_sum += nums[i]
        if curr_sum == 0:
            maxsize = i + 1
        try:
            maxsize = max(maxsize, i - dct[curr_sum])
        except KeyError:
            dct[curr_sum] = i
    return maxsize
print(findMaxLength([0, 1, 1]))

