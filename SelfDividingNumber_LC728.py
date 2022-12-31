class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if self.isSelfDividing(i):
                res.append(i)
        return res

    def isSelfDividing(self, num):
        for i in str(num):
            if i == '0' or num % int(i) != 0:
                return False
        return True