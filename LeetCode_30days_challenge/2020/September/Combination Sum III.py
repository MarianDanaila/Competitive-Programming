class Solution:
    def combinationSum3(self, k, n):
        results = []

        def backtrack(remain, comb, next_el):
            if remain == 0 and len(comb) == k:
                # valid combination
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # no valid combination
                return
            # Iterate through the reduced list of candidates
            for i in range(next_el, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()
        backtrack(n, [], 0)
        return results
