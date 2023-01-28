class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumA - sumB) // 2
        setB = set(bobSizes)
        for a in aliceSizes:
            if a - diff in setB:
                return [a, a - diff]