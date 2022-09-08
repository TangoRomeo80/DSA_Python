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

