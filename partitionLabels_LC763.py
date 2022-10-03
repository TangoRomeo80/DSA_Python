class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # count = {}
        # res = []
        # i, length = 0, len(s)
        # for j in range(length):
        #     c = s[j]
        #     count[c] = j

        # curLen = 0
        # goal = 0
        # while i < length:
        #     c = s[i]
        #     goal = max(goal, count[c])
        #     curLen += 1

        #     if goal == i:
        #         res.append(curLen)
        #         curLen = 0
        #     i += 1
        # return res

        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res