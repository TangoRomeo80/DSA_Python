class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # sort the score list
        sorted_score = sorted(score, reverse = True)
        # create a dictionary to store the score and its rank
        rank = {}
        for i in range(len(sorted_score)):
            if i == 0:
                rank[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank[sorted_score[i]] = "Bronze Medal"
            else:
                rank[sorted_score[i]] = str(i+1)
        # create a list to store the result
        result = []
        for i in range(len(score)):
            result.append(rank[score[i]])
        return result