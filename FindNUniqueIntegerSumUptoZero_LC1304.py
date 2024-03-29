class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        res = []
        if n % 2 != 0:
            res.append(0)
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        return res