class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        ans = []
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        sorted_keys = sorted(freq, key=freq.get, reverse=True)

        for key in sorted_keys:
            for _ in range(freq[key]):
                ans.append(key)

        return "".join(ans)
