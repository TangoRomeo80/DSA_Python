def reverseStringIter(s):
    for i in range(len(s)):
        print(s[len(s)-1-i])

def reverseStringRec(s):
    if len(s) == 0:
        return s
    else:
        return reverseStringRec(s[1:]) + s[0]

def reverseStringIter2(s):
    newString = ""
    for i in range(len(s)):
        newString = s[i] + newString
    return newString

