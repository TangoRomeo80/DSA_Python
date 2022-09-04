def removeAnagrams(words):
    def isAnagram(s, t):
        if len(s) != len(t):
            return False
        
        d = {}
    
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                d[i] = 1
        
        for i in d:
            if d[i] != 0:
                return False
            
        return True
        
    l, r = 0, 1
    while r < len(words):
        if isAnagram(words[l], words[r]):
            words.pop(r)
        else:
            l, r = l + 1, r + 1
                
    return words