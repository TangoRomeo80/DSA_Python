class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)
        # n = len(arr1)
        # create a dictionary to store the frequency of each element in arr1
        freq = {}
        for num in arr1:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        # create a list to store the result
        result = []
        # for each element in arr2, add it to the result list
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]
        # for each element in arr1 that is not in arr2, add it to the result list
        for num in sorted(freq.keys()):
            result.extend([num] * freq[num])
        return result