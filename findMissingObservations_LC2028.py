class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        nTotal = (mean * (n + m)) - sum(rolls)

        if nTotal < n or nTotal > 6 * n:
            return []
        
        res = []
        while nTotal:
            dice = min(nTotal - n + 1, 6)
            res.append(dice)
            nTotal -= dice
            n -= 1

        return res