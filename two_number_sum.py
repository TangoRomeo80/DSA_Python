#O(n^2) time | O(1) space implementation
def twoNumberSumNaive(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

#O(n) time | O(n) space implementation
def twoNumberSumHash(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


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



arr = [0, 1, 2, 3, 4, 5, 6]
target = 10

# print(twoNumberSumNaive(arr, target))
# print(twoNumberSumHash(arr, target))
# print(twoNumberSumSorted(arr, target))