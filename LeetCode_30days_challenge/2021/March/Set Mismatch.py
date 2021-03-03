from typing import List

# Approach 1 with Extra Space


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        ans = [0, 0]
        n = len(nums)
        for i in range(1, n+1):
            s.add(i)
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                ans[0] = num
        for num in s:
            ans[1] = num
        return ans

# Approach 2 with Constant Space


class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = 0
        for num in nums:
            if nums[abs(num)-1] < 0:
                dup = abs(num)
            else:
                nums[abs(num)-1] *= -1
        for i in range(n):
            if nums[i] > 0:
                return [dup, i+1]
