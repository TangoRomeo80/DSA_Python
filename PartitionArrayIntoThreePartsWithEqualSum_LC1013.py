class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 != 0:
            return False
        target = s // 3
        count = 0
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            if curr == target:
                count += 1
                curr = 0
        return count >= 3