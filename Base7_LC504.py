class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""
        neg = ''
        if num < 0:
            neg = '-'
            num = -num
        while num:
            ans += str(num % 7)
            num //= 7

        return neg + ans[::-1]

