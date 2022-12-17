class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        remaining, index = [x for x in range(1,n+1)], 0
        while remaining:
            index = (index+k-1) % len(remaining)
            result = remaining.pop(index)
        return result

