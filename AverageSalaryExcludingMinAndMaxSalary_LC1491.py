class Solution:
    def average(self, salary: List[int]) -> float:
        # salary.sort()
        # return sum(salary[1:-1])/(len(salary)-2)
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)