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



