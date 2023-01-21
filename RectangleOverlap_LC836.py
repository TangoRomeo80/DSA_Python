class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # if the two rectangles are not overlapping, then the leftmost point of the right rectangle must be to the left of the rightmost point of the left rectangle
        # and the bottommost point of the top rectangle must be below the topmost point of the bottom rectangle
        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1])