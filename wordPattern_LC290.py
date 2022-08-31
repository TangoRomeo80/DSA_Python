def wordPattern(pattern, s):
    words = s.split()
    if len(words) != len(pattern):
        return False
    d = {}
    for i in range(len(words)):
        if pattern[i] not in d:
            d[pattern[i]] = words[i]
        elif d[pattern[i]] != words[i]:
            return False
    return True