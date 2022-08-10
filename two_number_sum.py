#O(n^2) time | O(1) space implementation
def twoNumberSumNaive(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []



#O(n) time | O(n) space implementation
def twoNumberSumHash(nums, target):
    store = {}
    for i in range(len(nums) - 1):
        potentialMatch = target - nums[i]
        if potentialMatch in store:
            return [store[potentialMatch], i]
        else:
            store[nums[i]] = i
                
    return []

#O(n) time | O(n) space implementation that returns the indices of the two numbers
def twoNumberSumHashIndices(nums, target):
    store = {} #value: index
    for i,n in enumerate(nums):
        potentialMatch = target - n
        if potentialMatch in store:
            return [store[potentialMatch], i]
        store[n] = i
    return

#O(n log n) time | O(1) space implementation
def twoNumberSumSorted(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []



arr = [3, 2, 4]
target = 6

# print(twoNumberSumNaive(arr, target))
# print(twoNumberSumHash(arr, target))
# print(twoNumberSumSorted(arr, target))
print(twoNumberSumHashIndices(arr, target))