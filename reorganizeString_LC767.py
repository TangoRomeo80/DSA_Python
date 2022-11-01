from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) #hashmap counting each character occurances
        heap = [[-cnt, char]for char, cnt in count.items()]
        heapq.heapify(heap)

        prev = None
        res = ''
        while heap or prev:
            if prev and not heap:
                return ''

            # get most frequent except prev one
            cnt, char = heapq.heappop(heap)
            res += char
            cnt += 1
            # add prev one back to heap
            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res


