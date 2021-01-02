class Solution:
    def rotate(self, nums, k):
        copy_nums = nums.copy()
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = copy_nums[i]


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        # reverse all numbers
        for i in range(n // 2):
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]

        # reverse first k numbers
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]

        # reverse last n-k numbers
        for i in range(k, n - (n - k) // 2):
            nums[i], nums[n - i - 1 + k] = nums[n - i - 1 + k], nums[i]


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1
