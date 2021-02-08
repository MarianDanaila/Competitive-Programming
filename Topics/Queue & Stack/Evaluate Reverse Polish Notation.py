from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                first = stack.pop()
                second = stack.pop()
                if token == '+':
                    stack.append(second + first)
                elif token == '-':
                    stack.append(second - first)
                elif token == '*':
                    stack.append(second * first)
                else:
                    division = second // first

                    if second % first != 0 and division < 0:
                        division += 1
                    stack.append(division)
            else:
                stack.append(int(token))
        return stack[0]
