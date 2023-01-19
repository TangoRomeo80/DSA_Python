class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # split the sentence into words
        words = sentence.split()
        # create a list to store the new words
        new_words = []
        # loop through the words
        for i in range(len(words)):
            # if the word starts with a vowel, add "ma" to the end
            if words[i][0] in "aeiouAEIOU":
                new_words.append(words[i] + "ma")
            # if the word starts with a consonant, move the first letter to the end and add "ma"
            else:
                new_words.append(words[i][1:] + words[i][0] + "ma")
            # add "a" to the end of the word for each word in the sentence
            new_words[i] += "a" * (i + 1)
        # return the new words as a string
        return " ".join(new_words)