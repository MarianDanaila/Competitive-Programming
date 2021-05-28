class Solution:
    def maxProduct(self, words):
        mapping = {}
        for word in words:
            mapping[word] = set(word)
        max_value = 0
        n = len(words)
        for i in range(n - 1):
            set1 = mapping[words[i]]
            for j in range(i + 1, n):
                set2 = mapping[words[j]]
                good = True
                if len(set1) < len(set2):
                    for ch in set1:
                        if ch in set2:
                            good = False
                            break
                else:
                    for ch in set2:
                        if ch in set1:
                            good = False
                            break

                if good:
                    max_value = max(max_value, len(words[i]) * len(words[j]))
        return max_value
