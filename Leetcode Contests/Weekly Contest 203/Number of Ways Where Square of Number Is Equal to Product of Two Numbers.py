class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        cnt = 0
        dct1 = {}
        dct2 = {}
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                try:
                    dct1[nums1[i]*nums1[j]] += 1
                except KeyError:
                    dct1[nums1[i]*nums1[j]] = 1
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                try:
                    dct2[nums2[i]*nums2[j]] += 1
                except KeyError:
                    dct2[nums2[i]*nums2[j]] = 1

        for num in nums1:
            try:
                cnt += dct2[num*num]
            except KeyError:
                continue
        for num in nums2:
            try:
                cnt += dct1[num*num]
            except KeyError:
                continue
        return cnt
