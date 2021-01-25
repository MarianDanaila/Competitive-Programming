class Solution:
    def decodeString(self, s: str) -> str:
        mul = 1
        length = 0
        stack = []
        number = 0
        numbers = []
        for ch in s:
            if '0' <= ch <= '9':
                number = number * 10 + int(ch)
            elif ch == ']':
                mul //= stack.pop()
            elif ch == '[':
                numbers.append(number)
                stack.append(number)
                mul *= number
                number = 0
            else:
                length += mul
        output = [0] * length
        index = length - 1
        stck = []
        for i in range(len(s) - 1, -1, -1):
            if '0' <= s[i] <= '9':
                continue
            elif s[i] == ']':
                stck.append(index)
            elif s[i] == '[':
                lower = index
                upper = stck.pop()
                for _ in range(numbers.pop() - 1):
                    for j in range(upper, lower, -1):
                        output[index] = output[j]
                        index -= 1
            else:
                output[index] = s[i]
                index -= 1
        return ''.join(output)
