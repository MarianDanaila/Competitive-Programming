from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)

        answer = []
        if n == 1:
            for ch1 in buttons[int(digits[0])-2]:
                answer.append(ch1)
        elif n == 2:
            for ch1 in buttons[int(digits[0])-2]:
                for ch2 in buttons[int(digits[1])-2]:
                    answer.append(''.join([ch1, ch2]))
        elif n == 3:
            for ch1 in buttons[int(digits[0])-2]:
                for ch2 in buttons[int(digits[1])-2]:
                    for ch3 in buttons[int(digits[2])-2]:
                        answer.append(''.join([ch1, ch2, ch3]))

        elif n == 4:
            for ch1 in buttons[int(digits[0])-2]:
                for ch2 in buttons[int(digits[1])-2]:
                    for ch3 in buttons[int(digits[2])-2]:
                        for ch4 in buttons[int(digits[3])-2]:
                            answer.append(''.join([ch1, ch2, ch3, ch4]))

        return answer
