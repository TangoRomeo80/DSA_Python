def lengthOfLongestSubstring(s):
    # #O(n^3) solution (Gets TLE)
    # if len(s) == 0:
    #     return 0
    # if len(s) == 1:
    #     return 1
    # maxLen = 0
    # for i in range(len(s)):
    #     for j in range(i+1, len(s)+1):
    #         if len(set(s[i:j])) == len(s[i:j]):
    #             maxLen = max(maxLen, len(s[i:j]))
    # return maxLen

    # O(n) solution
    # Create a dictionary to store the last occurence of each character
    charSet = set()
    l = 0

    res = 0
    # Iterate through the string
    for r in range(len(s)):
        # If the character is not in the set, add it to the set
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r-l+1)

    return res