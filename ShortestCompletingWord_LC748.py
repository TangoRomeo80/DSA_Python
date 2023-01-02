class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # get the count of each letter in licensePlate
        count = {}
        for c in licensePlate:
            if c.isalpha():
                count[c.lower()] = count.get(c.lower(), 0) + 1
        
        # find the shortest word that has all the letters in licensePlate
        shortest = None
        for word in words:
            if not shortest or len(word) < len(shortest):
                if self.hasLetters(word, count):
                    shortest = word
        return shortest

    def hasLetters(self, word, count):
        for c in count:
            if word.count(c) < count[c]:
                return False
        return True