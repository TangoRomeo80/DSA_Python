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

