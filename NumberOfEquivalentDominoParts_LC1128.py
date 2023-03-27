class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # O(n^2)
        # count = 0
        # for i in range(len(dominoes)):
        #     for j in range(i+1, len(dominoes)):
        #         if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
        #             count += 1
        #         elif dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
        #             count += 1
        # return count

        # O(n)
        # step 1: count the dominoes
        d = {}
        for domi in dominoes:
            p = tuple(sorted(domi))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        c = 0
        for n in d.values():
            s = n*(n-1)//2
            c += s
        return c 
