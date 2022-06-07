#two numbers sum
def twoNumberSum(arr, target):
  nums = {}
  for num in arr:
    if (target - num) in nums:
      return [target - num, num]
    else:
      nums[num] = True
    return []

#validate subsequence
def validateSubsequence(arr, seq):
  seq_pointer = 0
  for num in arr:
    if num == seq[seq_pointer]:
      seq_pointer += 1
      if seq_pointer == len(seq):
        return True
  return False

#sorted square array
def sortedSquaredArray(arr):
  sortedSquares = [0 for _ in arr]
  left = 0
  right  = len(arr) - 1
  for i in reversed(range(len(arr))):
    if abs(arr[left]) > abs(arr[right]):
      sortedSquares[i] = arr[left]**2
      left += 1
    else:
      sortedSquares[i] = arr[right]**2
      right -= 1
  return sortedSquares
