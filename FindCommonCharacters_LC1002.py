import collections

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = collections.Counter(words[0])
        for word in words[1:]:
            count &= collections.Counter(word)
        return list(count.elements())