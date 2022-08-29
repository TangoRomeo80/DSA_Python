def pivotIndex(nums):
    if not nums:
        return -1
    if len(nums) == 1:
        return 0
    left_sum = 0
    right_sum = sum(nums)
    for i in range(len(nums)):
        if left_sum == right_sum - nums[i]:
            return i
        left_sum += nums[i]
        right_sum -= nums[i]
    return -1