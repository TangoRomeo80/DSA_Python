import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dict = {}
        banned = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()

        for word in paragraph:            
            if word not in banned:
                if word in dict:
                    dict[word]+=1
                else:
                    dict[word]=1
		#Don't need a counter if you use key function to choose the key with max. count!
        return max(dict, key=dict.get)