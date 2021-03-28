from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universal_words = []
        counter = {}
        for b in B:
            counter_b = Counter(b)
            for ch in counter_b:
                if ch not in counter:
                    counter[ch] = counter_b[ch]
                else:
                    counter[ch] = max(counter[ch], counter_b[ch])
        for a in A:
            counter_a = Counter(a)
            universal = True
            for ch in counter:
                if ch in counter_a and counter_a[ch] >= counter[ch]:
                    continue
                else:
                    universal = False
            if universal:
                universal_words.append(a)
        return universal_words
