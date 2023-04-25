class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        return ' '.join(s.split()[::-1])