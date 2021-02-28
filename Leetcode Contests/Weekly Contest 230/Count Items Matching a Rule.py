from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0
        for t, c, n in items:
            if ruleKey == "type" and t == ruleValue:
                counter += 1
            if ruleKey == "color" and c == ruleValue:
                counter += 1
            if ruleKey == "name" and n == ruleValue:
                counter += 1
        return counter
