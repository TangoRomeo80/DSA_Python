class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # 1. find the sqrt of the area
        # 2. find the largest L and W
        # 3. return the L and W
        sqrt = int(area ** 0.5)
        for i in range(sqrt, 0, -1):
            if area % i == 0:
                return [area // i, i]
        return [area, 1]