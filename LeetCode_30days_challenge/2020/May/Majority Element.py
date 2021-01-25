def majorityElement(nums):
    dct = {}
    for i in nums:
        try:
            dct[i] += 1
            if dct[i] > len(nums) / 2:
                return i
        except KeyError:
            dct[i] = 1

