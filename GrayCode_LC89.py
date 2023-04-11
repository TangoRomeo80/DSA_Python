class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        prev = self.grayCode(n - 1)
        result = prev[:]
        for i in range(len(prev) - 1, -1, -1):
            result.append(prev[i] + 2 ** (n - 1))
        return result

        
    