from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        nr_salaries = len(salary)
        sum_salaries = 0
        max_salary = 1000
        min_salary = 10 ** 6
        for i in range(nr_salaries):
            curr_salary = salary[i]
            sum_salaries += curr_salary
            min_salary = min(min_salary, curr_salary)
            max_salary = max(max_salary, curr_salary)
        return (sum_salaries - min_salary - max_salary) / (nr_salaries - 2)
