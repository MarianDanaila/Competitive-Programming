from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        length1 = len(nums1)
        length2 = len(nums2)
        op = i = j = 0
        if sum1 == sum2:
            return 0
        elif sum1 < sum2:
            if 6 * length1 < 1 * length2:  # -1 case
                return -1

            target = sum2 - sum1
            nums1.sort()
            nums2.sort(reverse=True)
            while i < length1 and j < length2:
                if nums1[i] == 6 and nums2[i] == 1:
                    break
                if 6 - nums1[i] >= nums2[j] - 1:
                    target -= 6 - nums1[i]
                    i += 1
                else:
                    target -= nums2[j] - 1
                    j += 1
                op += 1
                if target <= 0:
                    return op
            while i < length1:
                target -= 6 - nums1[i]
                op += 1
                i += 1
            while j < length2:
                target -= nums2[j] - 1
                op += 1
                j += 1
            return op

        else:
            if 1 * length1 > 6 * length2:  # -1 case
                return -1
            target = sum1 - sum2

            nums1.sort(reverse=True)
            nums2.sort()
            while i < length1 and j < length2:
                if nums1[i] == 1 and nums2[j] == 6:
                    break

                if nums1[i] - 1 >= 6 - nums2[j]:
                    target -= nums1[i] - 1
                    i += 1
                else:
                    target -= 6 - nums2[j]
                    j += 1

                op += 1
                if target <= 0:
                    return op
            while i < length1:
                target -= nums1[i] - 1
                op += 1
                i += 1
            while j < length2:
                target -= 6 - nums2[j]
                op += 1
                j += 1
            return op
