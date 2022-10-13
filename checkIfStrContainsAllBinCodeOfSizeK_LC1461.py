class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        binSet = set()
        for i in range(len(s) - k + 1):
            binSet.add(s[i:i+k])
        return len(binSet) == 2**k