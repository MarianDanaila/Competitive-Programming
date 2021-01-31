class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, -1, -1):
            min_bigger = float("inf")
            replace = -1
            for j in range(i + 1, n):
                if nums[i] < nums[j] < min_bigger:
                    min_bigger = nums[j]
                    replace = j
            if replace != -1:
                nums[i], nums[replace] = nums[replace], nums[i]
                break
        if replace == -1:
            for i in range(n // 2):
                nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
        else:
            for k in range(n - i - 1):
                swapped = False
                for l in range(i + 1, n - k - 1):
                    if nums[l] > nums[l + 1]:
                        nums[l], nums[l + 1] = nums[l + 1], nums[l]
                        swapped = True

                if not swapped:
                    break
