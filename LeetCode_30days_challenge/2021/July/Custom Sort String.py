from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        permutation = []
        counter = Counter(s)
        for ch in order:
            if ch in counter:
                occurrences = counter[ch]
                for _ in range(occurrences):
                    permutation.append(ch)
                counter.pop(ch)

        for ch in counter:
            occurrences = counter[ch]
            for _ in range(occurrences):
                permutation.append(ch)
        return "".join(permutation)
