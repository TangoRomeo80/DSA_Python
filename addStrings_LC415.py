class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = t = 0
        for i in range(len(num1)):
            num = int(num1[i])
            s = (s * 10) + num
        for i in range(len(num2)):
            num = int(num2[i])
            t = (t * 10) + num
        return str(s + t)
