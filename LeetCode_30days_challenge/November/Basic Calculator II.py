class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        s += ' '
        num = False
        for ch in s:
            if '0' <= ch <= '9':
                number = number * 10 + int(ch)
                num = True
            else:
                if num:
                    if len(stack) == 0:
                        stack.append(number)
                    else:
                        operator = stack[-1]
                        if operator == '*':
                            stack.pop()
                            last_number = stack.pop()
                            stack.append(last_number * number)
                        elif operator == '/':
                            stack.pop()
                            last_number = stack.pop()
                            stack.append(last_number // number)
                        elif operator == '+' or operator == '-':
                            stack.append(number)
                    number = 0
                    num = False
                if ch != ' ':
                    stack.append(ch)
        ans = stack[0]
        for i in range(1, len(stack) - 1, 2):
            if stack[i] == '+':
                ans += stack[i + 1]
            else:
                ans -= stack[i + 1]
        return ans
