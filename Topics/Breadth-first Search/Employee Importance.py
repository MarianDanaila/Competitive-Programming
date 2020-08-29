"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id) -> int:
        total_importance = 0
        company = {}
        for employee in employees:
            company[employee.id] = [employee.importance, employee.subordinates]
        stack = [id]
        while stack:
            employee = stack.pop()
            total_importance += company[employee][0]
            for subordinate in company[employee][1]:
                stack.append(subordinate)
        return total_importance
