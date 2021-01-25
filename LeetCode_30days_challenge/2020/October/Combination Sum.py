class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.backtracking(candidates, target, 0, [], res)
        return res

    def backtracking(self, nums, target, index, path, res):
        if target < 0:
            return  # backtrack
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.backtracking(nums, target-nums[i], i, path+[nums[i]], res)
