class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            s = self.countAndSay(n-1)
            count = 1
            result = ""
            for i in range(len(s)):
                if i == len(s)-1:
                    result += str(count) + s[i]
                elif s[i] == s[i+1]:
                    count += 1
                else:
                    result += str(count) + s[i]
                    count = 1
            return result

            