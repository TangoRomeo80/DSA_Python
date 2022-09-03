def reverseString(s):
    # for i in range(len(s) // 2):
    #     s[i], s[-i - 1] = s[-i -1], s[i]
    # return s

    # stack = []

    # for i in range(len(s)):
    #     stack.append(s[i])
    
    # for i in range(len(s)):
    #     s[i] = stack.pop()

    # return s

    # return s[::-1]

    # return s.reverse()

    def reverse(l, r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            reverse(l + 1, r - 1)

    reverse(0, len(s) - 1)

print(reverseString(['h','e','l','l','o']))