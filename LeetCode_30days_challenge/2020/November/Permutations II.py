from collections import Counter


class Solution:
    def permuteUnique(self, nums):
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
