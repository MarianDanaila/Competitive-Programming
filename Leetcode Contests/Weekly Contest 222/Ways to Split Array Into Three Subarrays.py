class Solution:
    def waysToSplit(self, nums):
        n = len(nums)
        prefix = []
        curr_sum = 0
        ans = 0
        for i in range(n):
            curr_sum += nums[i]
            prefix.append(curr_sum)
        # to find sum for a specific subarray [i:j] = prefix[j]-prefix[i-1] if i = 0 only prefix[j]
        for i in range(n - 2):
            left = prefix[i]
            low = i + 1
            high = n - 2
            leftmost = rightmost = -1
            while low <= high:
                m = low + (high - low) // 2
                mid = prefix[m] - prefix[i]
                right = prefix[-1] - prefix[m]
                if left <= mid <= right:
                    leftmost = m
                    high = m - 1
                elif left > mid:
                    low = m + 1
                else:
                    high = m - 1
            low = i + 1
            high = n - 2
            while low <= high:
                m = low + (high - low) // 2
                mid = prefix[m] - prefix[i]
                right = prefix[-1] - prefix[m]

                if left <= mid <= right:
                    rightmost = m
                    low = m + 1
                else:
                    if left > mid:
                        low = m + 1
                    else:
                        high = m - 1
            if leftmost != -1 and rightmost != -1:
                ans += rightmost - leftmost + 1
        return ans % (10 ** 9 + 7)
