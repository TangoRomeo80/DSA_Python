def isHappy(n):
    def isHappy(self, n: int) -> bool:
        visited= {}
        while n not in visited:
            visited[n] = True
            n = sum(int(i)**2 for i in str(n))
            if n == 1:
                return True
        return False