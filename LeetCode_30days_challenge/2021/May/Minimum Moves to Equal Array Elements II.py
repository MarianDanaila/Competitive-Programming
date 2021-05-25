class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        i = 0
        j = len(nums) - 1
        moves = 0
        while i < j:
            moves += nums[j] - nums[i]
            i += 1
            j -= 1
        return moves
