class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        if len(s) <= k:
            return s
        else:
            return self.licenseKeyFormatting(s[:-k], k) + '-' + s[-k:]