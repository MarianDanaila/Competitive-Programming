# Approach 1 using HEAP
# Time-complexity: O(N log k)
# Space complexity: O(N+k)
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        # Particular case of N = l
        # That ensures time complexity to be better than O(N log N)
        # Time complexity of below operation O(1)
        if k == len(nums):
            return nums
        # 1. build hash map: character and how oftein it appears
        # O(n) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)

# Approach 2: Quickselect
# Time-complexity: O(N) in the average case, O(N^2) in the worst case
# Space-complexty: O(N)
from collections import Counter
from random import randint
class Solution1:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            # move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]
            return store_index
        def quickselect(left, right, k_smallest):
            """
            Sort a list within left..right till kth less frequent elements
            takes its place
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index-1, k_smallest)
            # go right
            else:
                quickselect(pivot_index+1, right, k_smallest)
        n = len(unique)
        # kth top frequent element is (n-k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n-k)th less frequent element takes its final place (n-K) in a sorted array.
        # All elements on the left are less frequent.
        # All element on the right are more frequent
        quickselect(0, n-1, n-k)
        # return top k frequent elements
        return unique[n-k:]

# Approach 3 using Bucket sort
# Time-complexity: O(n)
# Space-complexity: O(n)

from itertools import chain
class Solution2:
    def topKFrequent(self, nums, k):
        print(nums)
        # 1. Create list of empty lists for buckets: for frequencies 1,2,..,n
        bucket =[[] for _ in range(len(nums)+1)]

        # 2. Use Counter to count frequencies of elements in nums
        count = Counter(nums)

        # 3. Iterate over our Counter and add elements to corresponding buckets
        for key in count:
            bucket[count[key]].append(key)

        # 4. buckets is a list of lists now, create one big list out of it
        flat_list = list(chain(*bucket))

        # 5. Finally, take the k last elements from this list, these elements will be top K frequent elements.
        print(flat_list[len(flat_list)-k:])

sol = Solution2()
sol.topKFrequent([1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5], 3)