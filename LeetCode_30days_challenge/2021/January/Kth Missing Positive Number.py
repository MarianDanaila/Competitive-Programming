class Solution:
    def findKthPositive(self, arr, k):
        diff = arr[0] - 1
        if diff >= k:
            return k
        k -= diff
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1] - 1
            if diff >= k:
                return arr[i - 1] + k
            k -= diff

        return arr[-1] + k
