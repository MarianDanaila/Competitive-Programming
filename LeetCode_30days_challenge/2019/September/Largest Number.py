# Approach1
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        compare = lambda a, b: -1 if a + b > b + a else 0
        return str(int("".join(sorted(map(str, nums), key=cmp_to_key(compare)))))


# Approach2
class Solution2:
    def largestNumber(self, nums):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if self.compare(str(nums[i]), str(nums[j])) == str(nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        if nums[0] == 0:
            return "0"
        out = ""
        for num in nums:
            out += str(num)
        return out

    def compare(self, nr1, nr2):
        if int(nr1 + nr2) <= int(nr2 + nr1):
            return nr2
        else:
            return nr1
