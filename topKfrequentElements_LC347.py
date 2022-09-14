import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # 1. create a dictionary to store the frequency of each element
        # 2. create a min heap to store the top k frequent elements
        # 3. iterate through the dictionary and push the elements into the heap
        # 4. pop the heap and return the result
        # Time complexity: O(nlogk)
        # Space complexity: O(n)
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # heap = []
        # for key, value in freq.items():
        #     heapq.heappush(heap, (value, key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # result = []
        # while heap:
        #     result.append(heapq.heappop(heap)[1])
        # return result

        #bucket sort with buckets mapped to number of occurences
        #time complexity: O(n)
        #space complexity: O(n)
        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i]:
                result += freq[i]
            if len(result) == k:
                return result