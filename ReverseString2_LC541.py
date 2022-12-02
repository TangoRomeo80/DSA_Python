class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return s
        s = list(s)
        i = 0
        while i < len(s):
            s[i:i+k] = reversed(s[i:i+k])
            i += 2*k
        return "".join(s)