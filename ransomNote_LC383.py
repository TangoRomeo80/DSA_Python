def canConstruct( ransomNote, magazine):
    for i in ransomNote:
        if i not in magazine:
            return False
        else:
            magazine = magazine.replace(i, '', 1)
                
    return True