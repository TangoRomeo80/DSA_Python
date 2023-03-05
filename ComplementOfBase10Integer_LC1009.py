class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        i = 0
        while n > 0:
            if n % 2 == 0:
                res += 2 ** i
            i += 1
            n //= 2
        return res