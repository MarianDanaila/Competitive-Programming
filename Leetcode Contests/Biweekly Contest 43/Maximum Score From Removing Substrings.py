class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        points = 0
        if x <= y:
            push_ch = 'b'
            pop_ch = 'a'
        else:
            push_ch = 'a'
            pop_ch = 'b'

        for ch in s:
            if ch == push_ch:
                stack.append(ch)
            elif ch == pop_ch:
                if not stack or stack[-1] == ch:
                    stack.append(ch)
                else:
                    stack.pop()
                    points += max(x, y)
            else:
                a = b = 0
                while stack:
                    last = stack.pop()
                    if last == 'a':
                        a += 1
                    else:
                        b += 1

                points += (min(x, y) * min(a, b))
        if stack:
            a = b = 0
            while stack:
                last = stack.pop()
                if last == 'a':
                    a += 1
                else:
                    b += 1
            points += (min(x, y) * min(a, b))
        return points
