class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 1. Initialize result to 0
        result = 0
        # 2. Iterate over the string
        for i in range(len(columnTitle)):
            # 3. Get the character
            char = columnTitle[i]
            # 4. Get the ASCII value of the character
            asciiValue = ord(char)
            # 5. Get the value of the character
            value = asciiValue - ord('A') + 1
            # 6. Multiply the value with 26 raised to the power of the index
            result += value * (26 ** (len(columnTitle) - i - 1))
        # 7. Return the result
        return result