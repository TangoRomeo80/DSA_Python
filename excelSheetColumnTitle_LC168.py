class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 1. Initialize result string
        result = ""
        # 2. Loop until columnNumber is 0
        while columnNumber:
            # 3. Get the remainder
            remainder = columnNumber % 26
            # 4. If remainder is 0, then add Z to result
            if remainder == 0:
                result = "Z" + result
                # 5. Update columnNumber
                columnNumber = columnNumber // 26 - 1
            # 6. Else, add the corresponding character to result
            else:
                result = chr(remainder + 64) + result
                # 7. Update columnNumber
                columnNumber = columnNumber // 26
        # 8. Return result
        return result