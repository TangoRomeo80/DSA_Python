class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = {}
        for i in range(len(morse)):
            morse_dict[chr(ord('a') + i)] = morse[i]
        morse_words = set()
        for word in words:
            morse_word = ''
            for char in word:
                morse_word += morse_dict[char]
            morse_words.add(morse_word)
        return len(morse_words)