def isPalindrome(self, x: int) -> bool:
    # return ((str(x) == str(x)[::-1]) and str(x)[0] != '-')
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
        
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x = x // 10
        
    return x == rev or x == rev // 10