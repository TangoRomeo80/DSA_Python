class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_gap = 0
        prev = None
        for i in range(len(binary)):
            if binary[i] == '1':
                if prev is not None:
                    max_gap = max(max_gap, i - prev)
                prev = i
        return max_gap