class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        count = 0
        for i in s:
            count += widths[ord(i) - ord('a')]
            if count > 100:
                line += 1
                count = widths[ord(i) - ord('a')]
        return [line, count]