from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        groups_str = []
        nums_str = "".join(map(str, nums))
        start = 0
        for group in groups:
            group_str = "".join(map(str, group))
            groups_str.append(group_str)
        for group_str in groups_str:
            idx = nums_str.find(group_str, start)
            if idx == -1:
                return False
            start = idx + len(group_str)
        return True
