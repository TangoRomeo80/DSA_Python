class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        res = ""
        for i in range(len(num1)):
            if i < len(num2):
                tmp = int(num1[i]) + int(num2[i]) + carry
            else:
                tmp = int(num1[i]) + carry
            carry = tmp // 10
            res += str(tmp % 10)
        if carry:
            res += str(carry)
        return res[::-1]
        
        # s = t = 0
        # for i in range(len(num1)):
        #     num = int(num1[i])
        #     s = (s * 10) + num
        # for i in range(len(num2)):
        #     num = int(num2[i])
        #     t = (t * 10) + num
        # return str(s + t)
