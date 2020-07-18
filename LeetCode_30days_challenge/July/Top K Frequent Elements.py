class Solution:
    def topKFrequent(self, nums, k):
        dct = {}
        ans = []
        for i in nums:
            try:
                dct[i] += 1
            except KeyError:
                dct[i] = 1
        sort_dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)

        for i in sort_dct:
            if k == 0:
                break
            ans.append(i[0])
            k -= 1
        return ans


solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))