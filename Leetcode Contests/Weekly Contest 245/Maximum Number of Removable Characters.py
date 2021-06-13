from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        """
        Just binary search the k value
        """
        n = len(removable)
        low, high = 0, n - 1
        len_s, len_p = len(s), len(p)
        maxim = 0
        while low <= high:  # binary search the biggest 'k' (in our case is mid)
            mid = low + (high - low) // 2
            arr = list(s)
            for i in range(mid + 1):
                arr[removable[i]] = ''  # simulate the removal
            new_s = "".join(arr)  # new string s after removing k characters
            idx1 = idx2 = 0
            new_len_s = len(new_s)
            while idx1 < new_len_s and idx2 < len_p:  # check if it is a subsequence
                if new_s[idx1] == p[idx2]:
                    idx2 += 1
                idx1 += 1
            if idx2 == len_p:  # it it's a subsequence we try bigger k next time, so we update the 'low'
                maxim = max(maxim, mid + 1)
                low = mid + 1
            else:
                high = mid - 1  # otherwise try smaller k
        return maxim
