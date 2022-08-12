def isPalindrome(s):
    filterStr = ''

    for i in s:
        if i.isalnum():
            filterStr += i.lower()

    for i in range(len(filterStr)//2):
        if filterStr[i] != filterStr[-i-1]:
            return False
    return True