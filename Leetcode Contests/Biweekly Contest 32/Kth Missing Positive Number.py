class Solution:
    def findKthPositive(self, arr, k) -> int:
        i = 1
        while k > 0:
            if i not in arr:
                k -= 1
            i += 1
        return i-1