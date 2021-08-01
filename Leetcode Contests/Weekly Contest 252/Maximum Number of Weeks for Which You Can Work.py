from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total_milestones = sum(milestones)
        maxim_milestone = max(milestones)
        diff = 2 * maxim_milestone - total_milestones
        if diff > 1:
            return total_milestones - diff + 1
        else:
            return total_milestones
