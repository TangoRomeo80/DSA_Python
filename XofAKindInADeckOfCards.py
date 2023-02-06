class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        deck.sort()
        count = 1
        for i in range(1, len(deck)):
            if deck[i] == deck[i - 1]:
                count += 1
            else:
                if count < 2:
                    return False
                else:
                    deck = deck[i:]
                    break
        if count < 2:
            return False
        for i in range(2, count + 1):
            if count % i == 0:
                for j in range(0, len(deck), i):
                    if deck[j:j + i] != [deck[j]] * i:
                        break
                else:
                    return True
        return False