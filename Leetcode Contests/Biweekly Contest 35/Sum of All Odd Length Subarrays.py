class Solution:
    def sumOddLengthSubarrays(self, arr):
        total_sum = 0
        for i in range(1, len(arr) + len(arr) % 2, 2):
            for j in range(len(arr) - i + 1):
                total_sum += sum(arr[j:j + i])
        return total_sum
