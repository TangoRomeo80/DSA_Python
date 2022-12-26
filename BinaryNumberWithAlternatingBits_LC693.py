class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0:
            return True
        prev = n % 2
        n = n // 2
        while n > 0:
            curr = n % 2
            if curr == prev:
                return False
            prev = curr
            n = n // 2
        return True