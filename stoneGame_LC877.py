
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Returning true gets accepted
        # Why??????
        # return True

        # This is a DP problem (O(n^2))
        dp= {} # subarray of piles (l, r) -> max of alice total

        # return max alice total
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            # Alice can take left or right
            # Alice wants to maximize her total
            # Bob wants to minimize Alice's total
            
            even = True if (r - l) % 2 else False
            # Alice picked left
            left = piles[l] if even else 0
            # Alice picked right
            right = piles[r] if even else 0

            dp[(l, r)] = max(dfs(l + 1, r) + left,
                             dfs(l, r - 1) + right)

            return dp[(l, r)]

        return dfs(0, len(piles) - 1) > sum(piles) // 2
