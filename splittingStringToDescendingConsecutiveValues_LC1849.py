class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev):
            if index == len(s):
                return True
            for i in range(index, len(s)):
                curr = int(s[index:i+1])
                if curr == prev - 1:
                    if dfs(i+1, curr):
                        return True
            return False


        for i in range(len(s) - 1):
            val = int(s[: i + 1])
            if dfs(i + 1, val):
                return True
        return False