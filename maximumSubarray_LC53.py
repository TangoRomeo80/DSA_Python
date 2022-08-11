def maxSubArrayCube(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            max_sum = max(max_sum, sum(nums[i:j+1]))
    return max_sum

def maxSubArraySquare(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

