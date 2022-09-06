def isPalindrome(self, x: int) -> bool:
    return ((str(x) == str(x)[::-1]) and str(x)[0] != '-')