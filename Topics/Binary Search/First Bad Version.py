# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                bad = mid
                high = mid - 1
            else:
                low = mid + 1
        return bad
