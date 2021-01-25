def subarraySum(nums, k):
    dct = {0: 1}
    sum = 0
    count = 0
    for i in nums:
        sum += i
        try:
            count += dct[sum-k]
        except KeyError:
            print("haha")
        try:
            dct[sum] += 1
        except KeyError:
            dct[sum] = 1
    return count


print(subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))