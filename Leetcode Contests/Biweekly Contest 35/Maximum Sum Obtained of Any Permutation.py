class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        freq = [0] * (n+1)
        for request in requests:
            freq[request[0]] += 1
            freq[request[1]+1] -= 1
        for i in range(1, n+1):
            freq[i] += freq[i-1]
        nums.sort(reverse=True)
        freq.sort(reverse=True)
        total_sum = 0
        for i in range(n):
            total_sum += nums[i] * freq[i]
        return total_sum % (10**9 + 7)
