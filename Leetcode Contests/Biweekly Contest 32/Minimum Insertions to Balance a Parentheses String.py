class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        l = 0
        r = 0
        right = 0
        diff = 0
        for i in s:
            if i == '(':
                l += 1
                diff += 2
                if right % 2 != 0:
                    insertions += 1
                    r += 1
                    diff -= 1
                right = 0
            else:
                r += 1
                right += 1
                diff -= 1
            if diff < 0:
                insertions += 1
                l += 1
                diff += 2
        if right % 2 != 0:
            insertions += 1
            r += 1
        # print(insertions)

        if l == r // 2:
            return insertions
        elif l < r // 2:
            return r // 2 - l + insertions
        else:
            return (l - r // 2) * 2 + insertions