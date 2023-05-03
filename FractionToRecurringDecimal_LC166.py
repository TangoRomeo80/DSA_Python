class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        if denominator == 0: return ""
        res = ""
        if (numerator < 0) ^ (denominator < 0):
            res += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        rem = numerator % denominator
        if rem == 0:
            return res
        res += "."
        mp = {}
        while rem != 0:
            if rem in mp:
                idx = mp[rem]
                part1 = res[:idx]
                part2 = res[idx:]
                res = part1 + "(" + part2 + ")"
                return res
            mp[rem] = len(res)
            rem *= 10
            res += str(rem // denominator)
            rem %= denominator
        return res