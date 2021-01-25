# Approach 1
# TC: O(M*N) where M is length of nums1 and N is length of nums2
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]
        for i in range(m, m + n):
            target = nums1[i]
            j = i - 1
            while target < nums1[j] and j >= 0:
                nums1[j + 1] = nums1[j]
                j -= 1
            nums1[j + 1] = target


# Approach 2
# TC: O(M+N) where M is the length of nums1 and N is the length of nums2
class Solution:
    def merge(self, nums1, m, nums2, n):
        i1 = m-1
        i2 = n-1
        j = m+n-1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] >= nums2[i2]:
                nums1[j] = nums1[i1]
                i1 -= 1
            else:
                nums1[j] = nums2[i2]
                i2 -= 1
            j -= 1
        while i2 >= 0:
            nums1[i2] = nums2[i2]
            i2 -= 1
