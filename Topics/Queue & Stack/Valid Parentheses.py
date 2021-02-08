class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif ch == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif ch == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            else:
                stack.append(ch)
        if not stack:
            return True
        return False
