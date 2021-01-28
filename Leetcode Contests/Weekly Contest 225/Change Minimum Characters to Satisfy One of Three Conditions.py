class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        case1 = case2 = 10 ** 5
        # case 3
        freq = [0] * 26
        for ch in a:
            freq[ord(ch) - 97] += 1

        for ch in b:
            freq[ord(ch) - 97] += 1

        most_common = max(freq)
        case3 = len(a) + len(b) - most_common

        # case 1 & 2
        for i in range(1, 26):
            changes1 = changes2 = 0
            for ch in a:
                if ch >= chr(i + 97):
                    changes1 += 1

            for ch in b:
                if ch < chr(i + 97):
                    changes1 += 1

            case1 = min(case1, changes1)

            for ch in a:
                if ch < chr(i + 97):
                    changes2 += 1

            for ch in b:
                if ch >= chr(i + 97):
                    changes2 += 1

            case2 = min(case2, changes2)

        return min(case1, case2, case3)
