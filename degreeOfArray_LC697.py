import collections

def findShortestSubArray(nums):
    degree = max(collections.Counter(nums).values())

    candidates = []

    for i in set(nums):
        if nums.count(i) == degree:
            candidates.append(len(nums) - nums[::-1].index(i) - nums.index(i))

    return min(candidates)