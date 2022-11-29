class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        for word in words:
            value = set(word.lower())
            if value <= set("qwertyuiop") or value <= set("asdfghjkl") or value <= set("zxcvbnm"):
                output.append(word)
        return output