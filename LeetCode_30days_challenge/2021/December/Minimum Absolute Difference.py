from typing import List


# Approach 1
# Two traversals
# TC: O(N), SC: O(N)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 2 * (10 ** 6)
        n = len(arr)
        pairs = []
        for i in range(1, n):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                pairs.append([arr[i - 1], arr[i]])
        return pairs


# Approach 2
# One traversal
# TC: O(N), SC:O(N)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 2 * (10 ** 6)
        n = len(arr)
        pairs = []
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                pairs.append([arr[i - 1], arr[i]])
            elif arr[i] - arr[i - 1] < min_diff:
                min_diff = arr[i] - arr[i - 1]
                pairs = [[arr[i - 1], arr[i]]]
        return pairs


# Approach 3
# Counting Sort
# TC: O(M + N), SC: O(M + N), where M - max element from array and N - min element from array
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minim = min(arr)
        maxim = max(arr)
        counting = [0] * (maxim - minim + 1)
        shift = minim
        for num in arr:
            counting[num - shift] = 1

        pairs = []
        prev = None
        min_diff = maxim - minim
        for i in range(maxim - minim + 1):
            if counting[i] == 1:
                if prev is None:
                    prev = i
                else:
                    if i - prev == min_diff:
                        pairs.append([prev + shift, i + shift])
                    elif i - prev < min_diff:
                        min_diff = i - prev
                        pairs = [[prev + shift, i + shift]]
                    prev = i
        return pairs
