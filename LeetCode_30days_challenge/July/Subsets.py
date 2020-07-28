# Approach 1: Cascading
# Time-complexity: O(N*(2^N))
# Space-complexity: O(N*(2^N))


class Solution:
    def subsets(self, nums):
        output = [[]]
        for i in range(len(nums)):
            for j in range(len(output)):
                if not output[j]:
                    output.append([nums[i]])
                else:
                    temp = output[j].copy()
                    temp.append(nums[i])
                    output.append(temp)
        return output

# Approach 2: Backtracking
# Time-complexity: O(N*(2^N))
# Space-complexity: O(N*(2^N))


class Solution2:
    def subsets(self, nums):
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i+1, curr)
                # backtrack
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return output