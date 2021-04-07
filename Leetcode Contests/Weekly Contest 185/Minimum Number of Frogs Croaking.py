class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = answer = frogs = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                frogs += 1
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            else:
                k += 1
                frogs -= 1

            if c >= r >= o >= a >= k:
                answer = max(answer, frogs)
            else:
                return -1

        if frogs == 0 and c == r == o == a == k:
            return answer
        return -1
