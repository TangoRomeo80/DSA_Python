def groupAnagrams(strs):
    # # O(m.nlogn) solution
    # # create a dictionary to store the anagrams
    # anagrams = {}
    # # loop through the list of strings
    # for s in strs:
    #     # sort the string
    #     sorted_s = ''.join(sorted(s))
    #     # if the sorted string is not in the dictionary, add it
    #     if sorted_s not in anagrams:
    #         anagrams[sorted_s] = [s]
    #     # if the sorted string is in the dictionary, append the string to the list
    #     else:
    #         anagrams[sorted_s].append(s)
    # # return the values of the dictionary
    # return anagrams.values()

    #O(m . n . 26) solution
    res = {} #mapping charCount to list of Anagrams

    for s in strs:
        charCount = [0] * 26 #26 letters in the alphabet
        for c in s:
            charCount[ord(c) - ord('a')] += 1
        if tuple(charCount) not in res:
            res[tuple(charCount)] = [s]
        else:
            res[tuple(charCount)].append(s)

    return res.values()

    

