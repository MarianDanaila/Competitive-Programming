# First Approach using Sorting
# Time-complexity: O(N log N)
# Space-complexity: O(1)
class Solution:
    def hIndex(self, citations) -> int:
        ok = True
        if not citations:
            return 0
        citations.sort(reverse=True)
        # We can also use binary search
        for i in range(len(citations)):
            if citations[i] < i+1:
                ok = False
                break
        if ok:
            return i+1
        else:
            return i

# Second Approach using Buckets
# Time-complexity: O(N)
# Space-complexity: O(N)
class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0 for _ in range(n+1)]
        for citation in citations:
            if citation >= n:
                buckets[n] += 1
            else:
                buckets[citation] += 1
        counter = 0
        for i in range(n, -1, -1):
            counter += buckets[i]
            if counter >= i:
                return i
        return 0