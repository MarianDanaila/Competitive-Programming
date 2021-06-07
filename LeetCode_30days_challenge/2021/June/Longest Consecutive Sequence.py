class Solution:
    def longestConsecutive(self, nums):
        set_nums = set(nums)
        longest_seq = 1
        for num in nums:
            if num - 1 not in set_nums:
                curr_seq = 1
                while num + 1 in set_nums:
                    curr_seq += 1
                    num += 1

                longest_seq = max(longest_seq, curr_seq)
        return longest_seq
