def wordPattern(pattern, s):
    words = s.split(' ')
    if len(words) != len(pattern):
        return False
        
    ctw = {}
    wtc = {}

    for c, w in zip(pattern, words):
        if c in ctw and ctw[c] != w:
            return False
        if w in wtc and wtc[w] != c:
            return False
        ctw[c] = w
        wtc[w] = c

    return True

    