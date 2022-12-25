from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        return ''.join([c * n for c, n in count.most_common()])

        