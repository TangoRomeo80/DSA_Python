def lengthOfLastWord(s):
    if not s:
        return 0
    s = s.strip()
    # return len(s.split(' ')[-1])
    length = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            length += 1
        else:
            break
    return length
