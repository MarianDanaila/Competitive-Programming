from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != '-' and token != '+' and token != '/' and token != '*':
                stack.append(int(token))
            else:
                first = stack.pop()
                if token == '+':
                    stack[-1] += first
                elif token == '-':
                    stack[-1] -= first
                elif token == '*':
                    stack[-1] *= first
                else:
                    if stack[-1] % first != 0 and stack[-1] // first < 0:
                        stack[-1] = stack[-1] // first + 1
                    else:
                        stack[-1] //= first

        return stack[0]
